import json
import requests
from bs4 import BeautifulSoup
import re
import os
from urllib.parse import urlparse

directory = 'data/temp/'

# откройте файл JSON и прочитайте существующие данные
with open(f"{directory}link_content.json", 'r', encoding="utf-8") as file:
    links = json.load(file)

headers = {
    "Accept":
    "*/*",
    "User-Agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0"
}
all_chapter_links = {}
# цикл по URL-адресам в файле JSON
for url in links.keys():
    parsed_url = urlparse(url)
    domain = parsed_url.scheme + '://' + parsed_url.netloc
    req = requests.get(url, headers=headers)
    src = req.text
    soup = BeautifulSoup(src, "lxml")
    ul_tag = soup.find('ul', {'class': 'chapter-list'})
    if ul_tag:
        for a_tag in ul_tag.find_all('a'):
            href = domain + a_tag.get('href')
            match = re.search(r'_(\d+)\.html', href)
            if match:
                title = match.group(1)
            all_chapter_links[href] = title

# записать обновленные данные в файл JSON
with open(f"{directory}all_chapter_links.json", 'w', encoding="utf-8") as file:
    json.dump(all_chapter_links, file, indent=4, ensure_ascii=False)
