import os
import shutil
from datetime import datetime

# Путь к исходной папке
source_folder = '/home/bonew/Рабочий стол/newPY/Python2/newPy'

# Путь к новой папке, куда будут скопированы файлы
destination_folder = '/home/bonew/Рабочий стол/newPY/Python2/new!!!!!'

# Получаем список всех файлов и подпапок в исходной папке
for root, dirs, files in os.walk(source_folder):
    for file_name in files:
        source_file_path = os.path.join(root, file_name)

        # Получаем дату создания файла
        creation_time = os.path.getctime(source_file_path)
        creation_date = datetime.utcfromtimestamp(creation_time).strftime('%Y-%m-%d')

        # Создаем папку с именем даты, если её нет
        date_folder = os.path.join(destination_folder, creation_date)
        os.makedirs(date_folder, exist_ok=True)

        # Копируем файл в соответствующую папку
        destination_file_path = os.path.join(date_folder, file_name)
        shutil.copy2(source_file_path, destination_file_path)

print("Файлы успешно скопированы и разложены по папкам с именем даты создания.")
