import fileinput

from src import get_website_content

def main():
    for line in fileinput.input():
        get_website_content(line)
    return 0

main()