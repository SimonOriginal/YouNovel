SPECIFIC_CHARCTERS = ["/", "\\", ":", "!", "?", "\"", "*", "<", ">"]


def get_filename(file_name):
    for character in SPECIFIC_CHARCTERS:
        file_name = file_name.replace(character, "")
    return file_name
