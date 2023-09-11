import os
import json
import csv
import pickle
from typing import List, Dict, Union

'''оригинальный код: https://github.com/bonew1988/Python2/blob/main/newPy/HW/24.08.2023/my_source/task_HW.py'''


class DirectoryInfo:
    def __init__(self, directory: str):
        self.directory = directory
        self.info = self.recursive_directory_info()

    def calculate_directory_size(self, directory: str) -> int:
        total_size = 0
        for dirpath, dirnames, filenames in os.walk(directory):
            for filename in filenames:
                filepath = os.path.join(dirpath, filename)
                total_size += os.path.getsize(filepath)
        return total_size

    def generate_file_info(self, filepath: str, parent_dir: str) -> Dict[str, Union[str, int]]:
        is_file = os.path.isfile(filepath)
        size = os.path.getsize(
            filepath) if is_file else self.calculate_directory_size(filepath)
        name = os.path.basename(filepath)
        parent = parent_dir if not is_file else os.path.basename(
            os.path.dirname(filepath))
        return {
            "name": name,
            "parent": parent,
            "type": "file" if is_file else "directory",
            "size": size
        }

    def recursive_directory_info(self) -> List[Dict[str, Union[str, int]]]:
        info = []
        for dirpath, _, filenames in os.walk(self.directory):
            for filename in filenames:
                filepath = os.path.join(dirpath, filename)
                info.append(self.generate_file_info(filepath, dirpath))
        return info

    def save_to_json(self, output_file: str) -> None:
        with open(output_file, "w") as f:
            json.dump(self.info, f, indent=4)

    def save_to_csv(self, output_file: str) -> None:
        with open(output_file, "w", newline="") as f:
            writer = csv.DictWriter(
                f, fieldnames=["name", "parent", "type", "size"])
            writer.writeheader()
            writer.writerows(self.info)

    def save_to_pickle(self, output_file: str) -> None:
        with open(output_file, "wb") as f:
            pickle.dump(self.info, f)

    def process(self, output_prefix: str) -> None:
        json_output = f"{output_prefix}.json"
        csv_output = f"{output_prefix}.csv"
        pickle_output = f"{output_prefix}.pickle"

        self.save_to_json(json_output)
        self.save_to_csv(csv_output)
        self.save_to_pickle(pickle_output)


if __name__ == "__main__":

    directory_to_scan = "/home/bonew/Рабочий стол/newPY/Python2/newPy/HW"
    output_file_prefix = "output_hw_01.09.2023"

    directory_info = DirectoryInfo(directory_to_scan)
    directory_info.process(output_file_prefix)
