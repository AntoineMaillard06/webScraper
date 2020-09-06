# module to get website content

import requests
import validators

def get_website_content(url: str):
    if validators.url(url):
        try:
            page = requests.get(url)
        except requests.ConnectionError as err:
            print("Connection Error: Probably a problem into url.\n", "\tExample: 'https://www.google.com/'")
        except requests.ConnectTimeout as err:
            print("Timed Out.")
    else:
        print("Url: ", url, "\tInvalid url.\n", "\tExample: 'https://www.google.com/'")
    print("---")
    return 0