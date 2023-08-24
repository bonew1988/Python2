import os
import json
import csv
import pickle
from typing import List, Dict, Union


def calculate_directory_size(directory: str) -> int:
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            total_size += os.path.getsize(filepath)
    return total_size


def generate_file_info(filepath: str, parent_dir: str) -> Dict[str, Union[str, int]]:
    is_file = os.path.isfile(filepath)
    size = os.path.getsize(
        filepath) if is_file else calculate_directory_size(filepath)
    name = os.path.basename(filepath)
    parent = parent_dir if not is_file else os.path.basename(
        os.path.dirname(filepath))
    return {
        "name": name,
        "parent": parent,
        "type": "file" if is_file else "directory",
        "size": size
    }


def recursive_directory_info(directory: str) -> List[Dict[str, Union[str, int]]]:
    info = []
    for dirpath, _, filenames in os.walk(directory):
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            info.append(generate_file_info(filepath, dirpath))
    return info


def save_to_json(info: List[Dict[str, Union[str, int]]], output_file: str) -> None:
    with open(output_file, "w") as f:
        json.dump(info, f, indent=4)


def save_to_csv(info: List[Dict[str, Union[str, int]]], output_file: str) -> None:
    with open(output_file, "w", newline="") as f:
        writer = csv.DictWriter(
            f, fieldnames=["name", "parent", "type", "size"])
        writer.writeheader()
        writer.writerows(info)


def save_to_pickle(info: List[Dict[str, Union[str, int]]], output_file: str) -> None:
    with open(output_file, "wb") as f:
        pickle.dump(info, f)


def main(directory: str, output_prefix: str) -> None:
    info = recursive_directory_info(directory)
    json_output = f"{output_prefix}.json"
    csv_output = f"{output_prefix}.csv"
    pickle_output = f"{output_prefix}.pickle"

    save_to_json(info, json_output)
    save_to_csv(info, csv_output)
    save_to_pickle(info, pickle_output)


if __name__ == "__main__":
    directory_to_scan = "path/to/your/directory"
    output_file_prefix = "output"
    main(directory_to_scan, output_file_prefix)
