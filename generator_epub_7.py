import ebooklib
from ebooklib import epub
import json
import os
from utills import get_filename

# Загрузите файл JSON
with open(f'data/temp/all_chapters.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
chapter_names = [item["chapter_name"] for item in data]
novel_name = data[0]["novel_name"]
# file_name = novel_name.replace("/", "").replace("\\", "").replace(":", "").replace(
#    "!", "").replace("?", "").replace("\"", "").replace("<", "").replace(">", "").replace("*", "")
file_name = get_filename(novel_name)
# Создайте книгу EPUB
book = epub.EpubBook()

# Установить метаданные книги
book.set_identifier('id123456')
# book.set_title(novel_name)
book.set_title(file_name)
book.set_language('en')
# Создать главу
with open(f"data/novel/{file_name}.txt", "r", encoding='utf-8') as file:
    chapter = epub.EpubHtml(
        title='Chapter 1', file_name='chap_01.xhtml', lang='en')
    chapter.content = file.read()
    book.add_item(chapter)

# Добавить главу в книгу
book.spine = ['nav', chapter]

# Create an empty chapter
book.add_item(epub.EpubNcx())
book.add_item(epub.EpubNav())

# Определить стиль CSS
style = 'BODY {color: white;}'
nav_css = epub.EpubItem(
    uid="style_nav", file_name="style/nav.css", media_type="text/css", content=style)

# Добавить файл CSS
book.add_item(nav_css)

# Create the EPUB file
epub.write_epub(f"data/novel/epub_novel/{file_name}.epub", book, {})
print(" Я закончил !")
