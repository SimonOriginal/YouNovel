import subprocess
import os

url = input(' Дай мне ссылку на историю, которую ты хочешь почитать: ')

with open(f"data/temp/url.txt", "w") as f:
    f.write(url)

result = subprocess.run(["python", "link_collector_button_1.py"])
if result.returncode == 0:
    print(" Работаем со ссылкой...")
    result = subprocess.run(["python", "link_collector_2.py"])
    if result.returncode == 0:
        print(" Выделяем текст из страниц!")
        result = subprocess.run(["python", "collector_chapter_3.py", url])
        if result.returncode == 0:
            print(" Склеиваем так, что не оторвешься!")
            result = subprocess.run(["python", "json_uniting_4.py"])
            if result.returncode == 0:
                print(" Делаем удобно для чтения ! ")
                result = subprocess.run(["python", "json_reader_5.py"])

                while True:
                    print(" 1. Вам перевести книгу")
                    print(" 2. Нет спасибо")
                    choice = input(" Введите свой выбор: ")
                    if choice == "1":
                        result = subprocess.run(["python", "translator_6.py"])
                        if result.returncode == 0:
                            print(" Делаем перплет для вашей книжечке ! ")
                            result = subprocess.run(
                                ["python", "generator_epub_7.py"])
                        break
                    elif choice == "2":
                        if result.returncode == 0:
                            print(" Делаем перплет для вашей книжечке ! ")
                            result = subprocess.run(
                                ["python", "generator_epub_7.py"])
                        break
                    else:
                        print(" Неверный выбор. Пожалуйста, попробуйте еще раз !")

json_folder_path = "data/json"
html_folder_path = "data/html"
temp_folder_path = "data/temp"


def clear_folder(folder_path):
    # удалить все файлы в папке
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        if os.path.isfile(file_path):
            os.unlink(file_path)

    # удалить все подкаталоги в папке
    for subdir_name in os.listdir(folder_path):
        subdir_path = os.path.join(folder_path, subdir_name)
        if os.path.isdir(subdir_path):
            os.rmdir(subdir_path)


clear_folder(json_folder_path)
clear_folder(html_folder_path)
clear_folder(temp_folder_path)

print(" Все временые файлы и каталоги очищенны ! ;)")
print(" Все скрипты заверщили работу! Приятного чтения ;)")
input("Нажмите Enter, чтобы выйти...")
