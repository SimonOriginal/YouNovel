import re
import sys
import requests
from bs4 import BeautifulSoup
import json
from urllib.parse import urlparse, parse_qs
import os

page_contents = int(input(' Введите количество переходов в оглавлении:'))
directory = 'data/temp/'

with open(f"{directory}url.txt", "r", encoding="utf-8") as f:
    url = f.read()

parsed_url = urlparse(url)
domain = parsed_url.scheme + '://' + parsed_url.netloc

parsed_url = urlparse(url)
query_params = parse_qs(parsed_url.query)
name_novel = re.search(r"novel/(.+)\.html", url).group(1)

# print(name_novel)

link_content = {}

for page_number in range(page_contents):
    full_href = domain + "/e/extend/fy.php?page=" + \
        str(page_number) + "&wjm=" + name_novel
#    print(" ", full_href)
    link_content[full_href] = page_number

json_data = json.dumps(link_content, indent=4, ensure_ascii=False)
with open(f"data/temp/link_content.json", "w", encoding="utf-8") as outfile:
    outfile.write(json_data)

print(" Ссылки на главы получены и сохранены !")
