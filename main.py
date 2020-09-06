import fileinput

from src.get_website_content import get_website_content

def main():
    for line in fileinput.input():
        print(line)
    return 0

main()