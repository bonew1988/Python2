# Задание №1
# Вспоминаем задачу 3 из прошлого семинара. Мы сформировали
# текстовый файл с псевдо именами и произведением чисел.
# Напишите функцию, которая создаёт из созданного ранее
# файла новый с данными в формате JSON.
# Имена пишите с большой буквы.
# Каждую пару сохраняйте с новой строки.
import json

__all__ = ['txt_to_json']


def txt_to_json(input_file: str, output_file: str):
    with open(input_file, 'r') as f:
        data = f.read(). split('\n')[:-1]
    data = [{i.split()[0].capitalize(): i.split()[1]} for i in data]
    print(data)
    with open(output_file, 'w') as res:
        json.dump(data, res, indent=4)


if __name__ == '__main__':
    txt_to_json('file_output.txt', 'outputfile.json')
