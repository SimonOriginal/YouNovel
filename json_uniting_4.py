import json
import os

# Папка, содержащая файлы JSON
folder = 'data/json'

# Инициализировать пустой список
json_files = []

# Получить список всех файлов в папке
all_files = os.listdir(folder)

# Сортировка списка файлов по номерам в заголовке
all_files.sort(key=lambda x: int(x.split(".")[0]))

# Итерация по отсортированному списку файлов
for file in all_files:
    # Проверьте, является ли файл файлом JSON.
    if file.endswith(".json"):
        # Откройте файл и прочитайте данные JSON.
        with open(os.path.join(folder, file), 'r', encoding="utf-8") as f:
            data = json.load(f)
        json_files.append(data)

# Объединить все файлы json в один
merged_json = []
for json_file in json_files:
    merged_json.extend(json_file)

# Запишите объединенные данные JSON в новый файл.
with open(f'data/temp/all_chapters.json', 'w',  encoding="utf-8") as f:
    json.dump(merged_json, f, indent=4, ensure_ascii=False)
