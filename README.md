# web_scraping_py
Some tests on web scraping with Python

# How to use it
___

Firstly, enter **complete website url**.
```
Enter the website's url you want to scrap:
> https://www.google.com/
```
→ Notified when content is get:
```
---
Website content has been get.
Command:
>
```
___

## Commands to get text

### Command to get all texts from web page
```
text
```

### Command to get all texts with specific word
```
text -w youtube
```

### Command to get all texts from specific element
```
text -e a
```
> This get all texts from \<a\>text\<\a\>

___

## Commands to get element

### Command to get all elements from web page
```
elem a
```
> This get all elements \<a\>\<\a\>

### Command to get all elements attribute
```
elem a -a href
```
> This get all href values from \<a\>\<\a\>
