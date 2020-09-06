# module to get element with command

import fileinput

from bs4 import BeautifulSoup

def scrap_page(content, input_stream):
    for line in input_stream:
        array_cmd = line.split()
    return 0