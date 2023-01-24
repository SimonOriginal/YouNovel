import json
import os
from utills import get_filename

# Load the JSON file
with open(f'data/temp/all_chapters.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Extract the "content", "chapter_name" and "novel_name" key from each object
contents = [item["content"] for item in data]
chapter_names = [item["chapter_name"] for item in data]
novel_name = data[0]["novel_name"]

# replace all double quotes with spaces
contents = [content.replace('\"', '\n') for content in contents]

# Create the folder path
folder_path = os.path.join("data", "novel")

# remove specific special characters from novel_name
file_name = get_filename(novel_name) + '.txt'
# file_name  = novel_name.replace("/", "").replace("\\", "").replace(":", "").replace("!", "").replace("?", "").replace("\"", "").replace("<", "").replace(">", "").replace("*", "") + '.txt'

file_path = os.path.join(folder_path, file_name)
# Create the output file name
name = '_'.join(novel_name.split())

# Write the contents and chapter names to a text file
with open(file_path, 'w', encoding='utf-8') as f:
    for i in range(len(contents)):
        f.write("Chapter " + chapter_names[i])
        for para in contents[i].split('\n'):
            if ":" not in para:
                f.write('   ' + para + '\n')
            else:
                f.write('   ' + para)
