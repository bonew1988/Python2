import os

__all__ = ['rename_files']


def rename_files(wanted_name: str, count_nums: int, extension_old: str, extension_new: str, diapazon: list[int], directory: str = ".") -> None:
    files_to_rename = [f for f in os.listdir(
        directory) if f.endswith(extension_old)]
    files_to_rename.sort()

    for idx, filename in enumerate(files_to_rename):
        original_name_part = filename[diapazon[0] - 1:diapazon[1]]
        new_number = str(idx + 1).zfill(count_nums)

        new_filename = f"{original_name_part}{wanted_name}{new_number}{extension_new}"
        new_filepath = os.path.join(directory, new_filename)
        old_filepath = os.path.join(directory, filename)

        os.rename(old_filepath, new_filepath)
        print(f"Переименовано {filename} в {new_filename}")
