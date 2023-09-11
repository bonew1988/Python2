from os import mkdir, getcwd, listdir
from random import randint, choice

__all__ = ['create_files']

def give_name() -> str:
    name: str = ''
    for _ in range(randint(4, 7)):
        name += chr(randint(98, 122))
    return name.capitalize()


def create_files(ext: str, directory: str = None, min_len: int = 6,
                 max_len: int = 30, min_size: int = 256,
                 max_size: int = 4096, count_files: int = 42):
    if not directory:
        directory = getcwd() + '\\'
    else:
        if directory not in listdir():
            mkdir(directory)
        directory = getcwd() + '\\' + directory + '\\'

    for _ in range(count_files):
        with open(directory + give_name() + ext, 'w',
                  encoding='utf-8') as output:
            list_of_bytes = bytes([randint(0, 255) for x in range(min_size,
                                                                  max_size)])

            output.write(str(list_of_bytes))


if __name__ == "__main__":
    EXTINSIONS = ['.pdf', '.csv', '.txt', '.doc']
    create_files(ext=choice(EXTINSIONS),
                 directory='test_dir\\test_test_dir', count_files=5)
