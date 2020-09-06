import fileinput
import json

from requests import models
from src import get_website_content, scrap_page

def main():
    input_stream = fileinput.input()
    print("Enter the website's url you want to scrap: ")
    for line in input_stream:
        page_content : models.Response = get_website_content(line)
        if page_content is not None:
            print("Website content has been get.")
            page_content = page_content.content
            if scrap_page(page_content, input_stream) == 0:
                break
        print("Enter the website's url you want to scrap: ")
    return 0

main()