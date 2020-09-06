# module to get element with command

import fileinput

from bs4 import BeautifulSoup

def scrap_page(content):
    for line in fileinput.input():
        print(line)
    return 0