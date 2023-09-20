import argparse
import nmap
import json
import ipaddress
import pandas as pd
import logging
import paramiko
from tqdm import tqdm
from timeout_decorator import timeout  # Добавляем библиотеку timeout_decorator

logging.basicConfig(filename='MY_log.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s: %(message)s')


class IPScanner:
    def __init__(self, start_ip, end_ip, output_file):
        self.start_ip = start_ip
        self.end_ip = end_ip
        self.output_file = output_file
        self.results = []

    def scan_ip(self, ip_address):
        nm = nmap.PortScanner()
        try:
            nm.scan(ip_address, arguments="-T4 -F")
        except nmap.PortScannerError as e:
            logging.error(
                f"Ошибка при сканировании IP-адреса {ip_address}: {str(e)}")
            return None

        result = {
            'ip_address': ip_address,
            'open_ports': [],
            'services': {}
        }

        try:
            for host in nm.all_hosts():
                open_ports = list(nm[host]['tcp'].keys())
                result['open_ports'] = open_ports

                for port, port_info in nm[host]['tcp'].items():
                    service_name = port_info['name']
                    service_product = port_info['product']
                    service_version = port_info['version']

                    result['services'][port] = {
                        'name': service_name,
                        'product': service_product,
                        'version': service_version
                    }
        except KeyError:
            pass

        logging.info(
            f"Открытые порты для IP-адреса {ip_address}: {', '.join(map(str, result['open_ports']))}")

        return result

    def scan_ip_range(self):
        start_ip_int = int(ipaddress.IPv4Address(self.start_ip))
        end_ip_int = int(ipaddress.IPv4Address(self.end_ip))

        for ip_int in tqdm(range(start_ip_int, end_ip_int + 1), desc="Сканирование IP"):
            ip = str(ipaddress.IPv4Address(ip_int))

            logging.info(f"Сканирование IP-адреса: {ip}")

            result = self.scan_ip(ip)
            if result:
                self.results.append(result)

        with open(self.output_file + '.json', 'w') as json_file:
            json.dump(self.results, json_file, indent=4)

        logging.info("Сканирование завершено")

        df = pd.DataFrame(self.results)
        excel_file = self.output_file + '.xlsx'
        df.to_excel(excel_file, index=False)

        print(
            f"Сканирование завершено. Результаты сохранены в {self.output_file}.json и {excel_file}")


@timeout(10)  # Установим тайм-аут в 10 секунд для авторизации
def ssh_login(ip_address, username, password):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip_address, port=22, username=username, password=password)
        ssh.close()
        logging.info(
            f"Успешная авторизация SSH на {ip_address} с логином '{username}' и паролем '{password}'")
        return True
    except Exception as e:
        logging.error(
            f"Не удалось авторизоваться SSH на {ip_address} с логином '{username}' и паролем '{password}': {str(e)}")
        return False


def main():
    logging.info("Начало работы программы")

    parser = argparse.ArgumentParser(description='IP Scanner')
    parser.add_argument('--start-ip', required=False,
                        help='Начальный IP-адрес')
    parser.add_argument('--end-ip', required=False, help='Конечный IP-адрес')
    parser.add_argument('--output-file', default='scan_results',
                        help='Имя файла для сохранения результатов')
    args = parser.parse_args()

    if args.start_ip and args.end_ip:
        start_ip = args.start_ip
        end_ip = args.end_ip
    else:
        start_ip, end_ip = input(
            "Введите начальный IP-адрес: "), input("Введите конечный IP-адрес: ")

    output_file = args.output_file

    scanner = IPScanner(start_ip, end_ip, output_file)
    scanner.scan_ip_range()

    for result in scanner.results:
        ip_address = result['ip_address']
        open_ports = result['open_ports']
        if 22 in open_ports:
            if ssh_login(ip_address, 'admin', 'admin'):
                print(
                    f"Успешная авторизация SSH на {ip_address} с логином 'admin' и паролем 'admin'")

    logging.info("Завершение работы программы")


if __name__ == "__main__":
    main()
