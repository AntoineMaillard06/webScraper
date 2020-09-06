# module to get element with command

import fileinput

from bs4 import BeautifulSoup
from src.utils import ( is_arg,
                        get_next_arg)
from src.cmd import (   cmd_text,
                        cmd_text_element,
                        cmd_text_wordline,
                        cmd_elem,
                        cmd_elem_attribute)

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
        if array_cmd[0] == "help":
            response["text"] += cmd_help()
        elif array_cmd[0] == "text":
            if len(array_cmd) == 1:
                response["text"] += cmd_text(content)
            elif is_arg(array_cmd, "-w"):
                response["text"] += cmd_text_wordline(content, get_next_arg(array_cmd, "-w"))
            elif is_arg(array_cmd, "-e"):
                response["text"] += cmd_text_element(content, get_next_arg(array_cmd, "-e"))
        elif array_cmd[0] == "elem":
            if len(array_cmd) == 2:
                response["text"] += cmd_elem(content, array_cmd[1])
            elif is_arg(array_cmd, "-a"):
                response["text"] += cmd_elem_attribute(content, array_cmd[1], get_next_arg(array_cmd, "-a"))
    exec_response(response)
    return 0