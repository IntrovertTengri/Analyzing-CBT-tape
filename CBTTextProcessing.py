import numpy as np
import re


def id_to_file_name(id, readme_or_about = 'readme'):
    if readme_or_about == 'readme':
        file_name = "./CBTREADMEs/" + str(id) + ".txt"
    elif readme_or_about == 'about':
        file_name = "./CBTAbouts/" + str(id) + ".txt"
    else:
        raise ValueError("readme or about")
    return file_name

def get_text_from_file(file_name):
    with open(file_name, "r") as file:
        header = file.readline().strip()
        id_length = len(re.sub("CBT", '', header))
        content = ''
        while True:
            line = file.readline()
            if not line:  # Stop if end of file
                break
            if line[0] == '/' and line[1] == '/':
                if line[2] == '*':
                    line = re.sub("//*", '', line)
                else:
                    line = re.sub("//", '', line)
            if id_length == 3:
                line = re.sub(r'\*{3}FILE \d{3}', '', line)
            else:
                line = re.sub(r'\*{4}FILE \d{4}', '', line)
            content = content + line
    file.close()
    return header, content

def preprocess_text(header, text):
    id_length = len(re.sub("CBT", '', header))
    substring = re.sub("CBT", "", header)
    substring = "FILE " + substring
    pattern = re.escape(substring)
    text = re.sub(pattern, '', text)
    text = re.sub("<code>", '', text)
    text = re.sub("</code>", '', text)
    text = re.sub(r'[*\/]', '', text)
    if id_length == 3:
        text = re.sub(r'\*{3}FILE \d{3}', '', text)
    else:
        text = re.sub(r'\*{4}FILE \d{4}', '', text)
    text = text.lower()
    text = re.sub(r'\s+', ' ', text).strip()
    return text
    