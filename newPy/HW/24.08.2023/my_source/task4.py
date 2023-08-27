# Задание №5
# Напишите функцию, которая ищет json файлы в указанной
# директории и сохраняет их содержимое в виде
# одноимённых pickle файлов.

import os
import json
import pickle

__all__ = ['convert_json_to_pickle']


def convert_json_to_pickle(json_dir):
    if not os.path.exists(json_dir):
        print(f"Директория '{json_dir}' не существует.")
        return

    for filename in os.listdir(json_dir):
        if filename.endswith('.json'):
            json_path = os.path.join(json_dir, filename)
            pickle_path = os.path.join(
                json_dir, filename.replace('.json', '.pickle'))

            with open(json_path, 'r', encoding='UTF-8') as json_file:
                data = json.load(json_file)

            with open(pickle_path, 'wb') as pickle_file:
                pickle.dump(data, pickle_file)

            print(
                f"Файл '{json_path}' преобразован и сохранен как '{pickle_path}'.")


if __name__ == '__main__':
    json_directory = '/home/bonew/Рабочий стол/NewPython/'
    convert_json_to_pickle(json_directory)
