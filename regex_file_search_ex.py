import re

""" GIven list of files, find all the files  which which are of type jpg """
items = [
    "photos",
    "documents",
    "videos",
    "image001.jpg",
    "image002.jpg",
    "image005.jpg",
    "wallpaper.jpg",
    "flower.jpg",
    "earth.jpg",
    "monkey.jpg",
    "image002.png",
]

# Let's create a string from the list of files
items = " ".join(items)

# Create a pattern to find all the files with ext .jpg
pattern = re.compile(r"(\b\w+[.]jpg\b)")

print(pattern.findall(items))
