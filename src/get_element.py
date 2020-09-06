# module to get element with command

import fileinput

from bs4 import BeautifulSoup
from src.utils import ( is_arg,
                        get_next_arg)
from src.cmd import (   cmd_text,
                        cmd_text_attribute,
                        cmd_text_wordline)

def cmd_help():
    print("How to use it:\n")
    return 0

def exec_response(response):
    print(response["text"])
    if response["file"] and len(response["filename"]) > 0:
        f = open(response["filename"], "a")
        f.write(response["text"])
        f.close()
    return 0

def scrap_page(content, input_stream):
    content = BeautifulSoup(content, 'html.parser')
    response = {
        "text": "",
        "file": False,
        "filename": ""
    }

    for line in input_stream:
        array_cmd = line.split()
        if is_arg(array_cmd, "-f"):
            response["file"] = True
            response["filename"] = get_next_arg(array_cmd, "-f")
        if array_cmd[0] == "help" or array_cmd[0] == "h":
            response["text"] += cmd_help()
        elif array_cmd[0] == "text" or array_cmd[0] == "t":
            if len(array_cmd) == 1:
                response["text"] += cmd_text(content)
            elif is_arg(array_cmd, "-w"):
                response["text"] += cmd_text_wordline(content, get_next_arg(array_cmd, "-w"))
            elif is_arg(array_cmd, "-a"):
                response["text"] += cmd_text_attribute(content, get_next_arg(array_cmd, "-a"))
    exec_response(response)
    return 0