# Напишите следующие функции:

# Нахождение корней квадратного уравнения
# Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.
# Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла.
# Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.

import csv
import json
import random
import math


def save_to_json(func):
    '''Декоратор для сохранения параметров и результатов работы функции в json файл'''
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        data = {
            "parameters": (args, kwargs),
            "result": result
        }
        with open('results.json', 'w') as json_file:
            json.dump(data, json_file, indent=4)
        return result
    return wrapper


def solve_square_equation(func):
    '''Декоратор для нахождения корней квадратного уравнения с каждой тройкой чисел'''
    def wrapper(numbers):
        results = []
        for a, b, c in numbers:
            discriminant = b**2 - 4*a*c
            if discriminant >= 0:
                root1 = (-b + math.sqrt(discriminant)) / (2*a)
                root2 = (-b - math.sqrt(discriminant)) / (2*a)
                results.append((root1, root2))
            else:
                results.append(None)
        return results
    return wrapper


def generate_csv(filename, num_rows):
    '''Генерация CSV файла'''
    with open(filename, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        for _ in range(num_rows):
            row = [random.randint(1, 1000) for _ in range(3)]
            csv_writer.writerow(row)


def read_csv(filename):
    '''Функция для чтения CSV файла и возврата списка троек чисел'''
    numbers = []
    with open(filename, 'r') as csvfile:
        csv_reader = csv.reader(csvfile)
        for row in csv_reader:
            a, b, c = map(int, row)
            numbers.append((a, b, c))
    return numbers


@save_to_json
@solve_square_equation
def find_roots(numbers):
    return numbers


if __name__ == "__main__":
    csv_filename = 'data.csv'
    generate_csv(csv_filename, num_rows=100)
    numbers = read_csv(csv_filename)
    roots = find_roots(numbers)
    print("Roots:", roots)
