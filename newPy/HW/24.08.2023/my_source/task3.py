# Задание №3
# Напишите функцию, которая сохраняет созданный в
# прошлом задании файл в формате CSV

import json
import csv

__all__ = ['json_to_csv', 'csv_to_json']


def json_to_csv(filename: str):
    with open(f'{filename}.json', 'r') as f_inp:
        data = json.load(f_inp)
    rows = []
    for level, users in data.items():
        for id, name in users.items():
            rows.append({'level': level,
                         'name': name,
                         'id': id})
    with open(f'{filename}.csv', 'w', newline='') as res:
        csv_write = csv.DictWriter(res, fieldnames=['level',
                                                    'name',
                                                    'id'])
        csv_write.writeheader()
        csv_write.writerows(rows)


def csv_to_json(filename: str):
    with open(f'{filename}.csv', 'r', newline='') as f_csv:
        data = f_csv.read().split('\n')
        print(data)

    res: list = []
    data.pop()
    for value in data[1:]:
        print(value)
        level, name, id = value[:-1].split(',')
        res.append({"id": f"{int(id):06}", "level": level,
                   "name": name, "hash": hash(id+name)})

    with open(f'task5_{filename}.json', 'w', newline='') as f_json:
        json.dump(res, f_json, indent=4)


if __name__ == '__main__':
    json_to_csv('users')
    csv_to_json('users')
