import fileinput
import json

from requests import models
from src import get_website_content

def main():
    for line in fileinput.input():
        page_content : models.Response = get_website_content(line)
        if page_content is not None:
            page_content = page_content.content
    return 0

main()