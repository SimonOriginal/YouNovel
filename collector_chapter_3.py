import asyncio
import random
import aiohttp
from bs4 import BeautifulSoup
import json
from tqdm import tqdm


async def fetch_chapter(session, url, headers, count, chapter_name):
    async with session.get(url, headers=headers) as resp:
        src = await resp.text()
        with open(f"data/html/{chapter_name}.html", "w", encoding='utf-8') as file:
            file.write(src)

        with open(f"data/html/{chapter_name}.html", encoding='utf-8') as file:
            src = file.read()

        soup = BeautifulSoup(src, "lxml")
        chapter_content = soup.find(class_="chapter-content")
        chapter_content_p = chapter_content.text

        if chapter_content_p is None:
            print("Ошибка: не удалось найти элемент с классом 'chapter-content'.")
            return
        h1_tag = soup.find('div', {'class': 'titles'})
        for novel_name in h1_tag.find_all('a'):
            novel_name_n = novel_name.get('title')

        json_data = [{
            "novel_name": novel_name_n,
            "chapter_name": chapter_name,
            "content": chapter_content_p
        }]
        with open(f"data/json/{count}.json", "w", encoding='utf-8') as file:
            json.dump(json_data, file, indent=10, ensure_ascii=False)
#        print(" Выделяем текст из главы", chapter_name, "и ведем запись...", end='\r', flush=True)


async def main():

    with open(f"data/temp/url.txt", "r") as f:
        url = f.read()
    headers = {
        "Accept":
        "*/*",
        "User-Agent":
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0"
    }

    # загрузить данные из json-файла
    with open(f'data/temp/all_chapter_links.json', encoding='utf-8') as file:
        all_chapter = json.load(file)

    iteration_count = int(len(all_chapter))
    count = 1
    print(f" Количесво глав для чтения: {iteration_count}")
    with tqdm(total=iteration_count, leave=True) as pbar:
        async with aiohttp.ClientSession() as session:
            tasks = []
            for chapter_href, chapter_name in all_chapter.items():
                # Оставьте только числовые символы в название_главы
                chapter_name = "".join(
                    c for c in chapter_name if c.isnumeric())
    # Сделайте что-нибудь с главой_href и главой_названием

                task = asyncio.ensure_future(fetch_chapter(
                    session, chapter_href, headers, count, chapter_name))
                tasks.append(task)
                count += 1
                iteration_count = iteration_count - 1
                await asyncio.sleep(random.randrange(1, 3))
                pbar.update(1)
            await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())
