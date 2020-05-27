import re

### Visualize you r regex expression
### https://regexper.com/#%28%5Cb%5Cw%2B%5B%40%5D%5Ba-z%5D%7B3%2C5%7D%5B.%5Dcom%5Cb%29


""" Given list of files, find all the files  which which are of type jpg """
items = [
    "photos",
    "documents",
    "videos",
    "image001.jpg",
    "image002.jpg",
    "image005.jpg",
    "wallpaper.jpg",
    "image111.png",
    "test111.doc",
    "flower.jpg",
    "earth.jpg",
    "monkey.jpg",
    "image002.png",
]

# Let's create a string from the list of files
items = " ".join(items)

# Compile a pattern to find all the files which ends with ext .jpg
pattern = re.compile(r"(\b\w+[.]jpg\b)")
# print all the files which have ext jpg
print(pattern.findall(items))


# Compile a pattern to recognise the files with ext jpg and start with word 'image'
pattern = re.compile(r"(\bimage\w+[.]jpg\b)")
print(pattern.findall(items))
