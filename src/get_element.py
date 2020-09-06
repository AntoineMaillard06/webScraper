# module to get element with command

import fileinput

from bs4 import BeautifulSoup
from src.utils import ( is_arg,
                    get_next_arg)

def cmd_help():
    print("How to use it:\n")
    return 0

def cmd_text(content):
    return content.get_text()

def cmd_wordline(content, word):
    text = content.get_text().split('\n')
    response = word + " match(s):\n"

    for line in text:
        if word.lower() in line.lower():
            response += line + '\n'
    return response

def scrap_page(content, input_stream):
    content = BeautifulSoup(content, 'html.parser')

    for line in input_stream:
        array_cmd = line.split()
        response = {
            "text": "",
            "file": False,
            "filename": ""
        }
        if is_arg(array_cmd, "-f"):
            response["file"] = True
            response["filename"] = get_next_arg(array_cmd, "-f")
        if array_cmd[0] == "help" or array_cmd[0] == "h":
            response["text"] += cmd_help()
        elif array_cmd[0] == "text" or array_cmd[0] == "t":
            if len(array_cmd) == 1:
                response["text"] += cmd_text(content)
            elif is_arg(array_cmd, "-w"):
                response["text"] += cmd_wordline(content, get_next_arg(array_cmd, "-w"))
        print(response["text"])
    return 0