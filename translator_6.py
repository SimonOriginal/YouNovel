import os
from deep_translator import GoogleTranslator
from tqdm import tqdm
import json
from utills import get_filename


def translate_file(dest_lang):

    with open(f'data/temp/all_chapters.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    novel_name = data[0]["novel_name"]
    file_path = get_filename(novel_name) + '.txt'
    # file_path = novel_name.replace("/", "").replace("\\", "").replace(":", "").replace(
    #    "!", "").replace("?", "").replace("\"", "").replace("<", "").replace(">", "").replace("*", "")

    # прочитать текст из файла
    with open(f'data/novel/' + file_path, 'r', encoding='utf-8') as f:
        text = f.read()

    # Разбить текст на куски длиной менее 5000 символов
    MAX_CHUNK_LENGTH = 4950
    chunks = [text[i:i+MAX_CHUNK_LENGTH]
              for i in range(0, len(text), MAX_CHUNK_LENGTH)]

    translated_text = ''
    total_chunks = len(chunks)
    for i, chunk in tqdm(enumerate(chunks), total=total_chunks):
        try:
            translated_text += GoogleTranslator(source='auto',
                                                target=dest_lang).translate(chunk)
        except:
            print(" Ошибка перевода этого фрагмента, повторная попытка...")
            translated_text += GoogleTranslator(source='auto',
                                                target=dest_lang).translate(chunk)
    # Write translated text to new file

    new_file_path = f'data/novel/{file_path}'

    with open(new_file_path + '.txt', 'w', encoding='utf-8') as f:
        f.write(translated_text)
    print(" Перевод завершен.")


if __name__ == '__main__':
    #    file_path = input("Введите название истории для перевода: ")

    dest_lang = input(" Язык на который нужно перевести: ")

    result = translate_file(dest_lang)
