# module to get website content

import requests

def get_website_content(url: str):
    page = None

    try:
        page = requests.get(url.replace('\n', ''))
    except requests.ConnectionError as err:
        print("Connection Error: Probably a problem into url.\n", "\tExample: 'https://www.google.com/'")
    except requests.ConnectTimeout as err:
        print("Timed Out.")
    print("---")
    return page