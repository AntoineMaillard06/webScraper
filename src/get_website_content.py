# module to get website content

import requests
import validators

def get_website_content(url: str):
    if validators.url(url):
        try:
            page = requests.get(url)
        except:
            print("Website content cannot be get.")
    else:
        print("Url: ", url, "\tInvalid url.\n", "\tExample: 'https://www.google.com/'")
    print("---")
    return 0