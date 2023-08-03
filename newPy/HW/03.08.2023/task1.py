# Напишите функцию, которая принимает на вход строку — абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.

import os


def split_file_path(file_path: str) -> tuple:
    path, full_filename = os.path.split(file_path)
    filename, extension = os.path.splitext(full_filename)
    return path, filename, extension


file_path = "test_dir/Bzmx.pdf"
path, filename, extension = split_file_path(file_path)
print("Путь:", path)
print("Имя файла:", filename)
print("Расширение файла:", extension)
