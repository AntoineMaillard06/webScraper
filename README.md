# webScraper
Some tests on web scraping with Python

# How to exec it
___
```
chmod 777 webScraper
./webScraper
```

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
> You can use multiple words on this.
```
text -w youtube gmail
```

### Command to get all texts from specific element
```
text -e a
```
> This get all texts from \<a\>text\<\a\>, you can use multiple elements on this.
```
text -e a p h1
```
___

## Commands to get element

### Command to get all elements from web page
```
elem a
```
> This get all elements \<a\>\<\a\>, you can use multiple elements on this.
```
elem a p h3
```

### Command to get all elements attribute
```
elem a -a href
```
> This get all href values from \<a\>\<\a\>, you can use multiple elements on this.
```
elem a h4 p -a class
```

___

## Commands to write in a file
```
text -f filename
```
___

## Command to use tool on an other website
```
next
```
