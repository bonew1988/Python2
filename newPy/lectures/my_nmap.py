import nmap
import json
import ipaddress
import pandas as pd  # Добавляем библиотеку pandas
from tqdm import tqdm  # Импортируем tqdm для создания прогресс-бара

# Функция для ввода и проверки IP-адресов


def get_ip_range():
    while True:
        try:
            start_ip = input("Введите начальный IP-адрес: ")
            end_ip = input("Введите конечный IP-адрес: ")

            # Проверка корректности IP-адресов
            ipaddress.IPv4Address(start_ip)
            ipaddress.IPv4Address(end_ip)

            return start_ip, end_ip
        except ipaddress.AddressValueError:
            print(
                "Один из введенных IP-адресов некорректен. Пожалуйста, введите корректные IP-адреса.")

# Функция для сканирования IP-адреса и получения информации о портах и сервисах


def scan_ip(ip_address):
    nm = nmap.PortScanner()
    nm.scan(ip_address, arguments="-T4 -F")  # Сканирование быстрыми опциями

    result = {
        'ip_address': ip_address,
        'open_ports': [],
        'services': {}
    }

    try:
        for host in nm.all_hosts():
            open_ports = nm[host]['tcp'].keys()
            result['open_ports'] = list(open_ports)

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

    return result

# Функция для сканирования диапазона IP-адресов


def scan_ip_range(start_ip, end_ip, output_file):
    results = []

    # Преобразуем IP-адреса в числа для выполнения сканирования в диапазоне
    start_ip_int = int(ipaddress.IPv4Address(start_ip))
    end_ip_int = int(ipaddress.IPv4Address(end_ip))

    for ip_int in tqdm(range(start_ip_int, end_ip_int + 1), desc="Сканирование IP"):
        ip = str(ipaddress.IPv4Address(ip_int))
        result = scan_ip(ip)
        results.append(result)

    # Сохраняем результаты в JSON-файл
    with open(output_file + '.json', 'w') as json_file:
        json.dump(results, json_file, indent=4)

    # Создаем DataFrame из данных JSON
    df = pd.DataFrame(results)

    # Сохраняем DataFrame в Excel-файл
    excel_file = output_file + '.xlsx'
    df.to_excel(excel_file, index=False)

    print(
        f"Сканирование завершено. Результаты сохранены в {output_file}.json и {excel_file}")


if __name__ == "__main__":
    # Получаем начальный и конечный IP-адреса от пользователя
    start_ip, end_ip = get_ip_range()

    # Задайте имя для файла вывода (без расширения)
    output_file = 'scan_results'

    # Вызываем функцию для сканирования диапазона IP-адресов
    scan_ip_range(start_ip, end_ip, output_file)
