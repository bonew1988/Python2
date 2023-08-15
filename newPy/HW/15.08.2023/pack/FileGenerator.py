import os
import random
import string

__all__ = ['create_random_files']


def generate_random_filename(length):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for _ in range(length))


def create_random_files(directory, num_files, name_list, extensions):
    if not os.path.exists(directory):
        os.makedirs(directory)

    for i in range(1, num_files + 1):
        random_name = random.choice(name_list)
        random_extension = random.choice(extensions)
        file_name = f"{random_name}_{i}.{random_extension}"
        file_path = os.path.join(directory, file_name)

        with open(file_path, 'w') as file:
            file.write("просто так")

        print(f"Создан файл: {file_path}")
