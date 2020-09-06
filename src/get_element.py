# module to get element with command

import fileinput

from bs4 import BeautifulSoup
from src.utils import ( is_arg,
                        get_next_arg,
                        get_next_args)
from src.cmd import (   cmd_text,
                        cmd_text_elements,
                        cmd_text_wordlines,
                        cmd_elems,
                        cmd_elem_attributes)

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

    print("Command:")
    for line in input_stream:
        response = {
            "text": "",
            "file": False,
            "filename": ""
        }
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
                response["text"] += cmd_text_wordlines(content, get_next_args(array_cmd, "-w"))
            elif is_arg(array_cmd, "-e"):
                response["text"] += cmd_text_elements(content, get_next_args(array_cmd, "-e"))
        elif array_cmd[0] == "elem":
            if is_arg(array_cmd, "-a"):
                array_cmd.pop(0)
                response["text"] += cmd_elem_attributes(content, get_next_args(array_cmd), get_next_arg(array_cmd, "-a"))
            else:
                array_cmd.pop(0)
                response["text"] += cmd_elems(content, array_cmd)
        elif array_cmd[0] == "next":
            exec_response(response)
            return 1
        exec_response(response)
        print("Command:")
    return 0