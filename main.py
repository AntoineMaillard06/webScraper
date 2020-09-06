import fileinput
import json

from requests import models
from src import get_website_content, scrap_page

def main():
    print("Enter the website's url you want to scrap: ")
    for line in fileinput.input():
        page_content : models.Response = get_website_content(line)
        if page_content is not None:
            page_content = page_content.content
            scrap_page(page_content)
        print("Enter the website's url you want to scrap: ")
    return 0

main()