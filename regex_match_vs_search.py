import re


def match_pattern(text, patterns):
    if re.match(patterns, text):
        return re.match(patterns, text)
    else:
        return "Not found!"


def find_pattern(text, patterns):
    if re.search(patterns, text):
        return re.search(patterns, text)
    else:
        return "No Match Found!"


print(find_pattern("aabbcc", "b+"))  # match bb
print(match_pattern("aabbcc", "b+"))  # no match


line = "Cats are smarter than dogs"
searchObj = re.search(r"(.*) are (.*?) .*", line, re.M | re.I)

if searchObj:
    print("searchObj.group() : ", searchObj.group())
    print("searchObj.group(1) : ", searchObj.group(1))
    print("searchObj.group(2) : ", searchObj.group(2))
else:
    print("Nothing found!!")

line = "Cats are smarter than dogs"
matchObj = re.match(r"(.*) are (.*?) .*", line, re.M | re.I)

if searchObj:
    print("matchObj.group() : ", matchObj.group())
    print("matchObj.group(1) : ", matchObj.group(1))
    print("matchObj.group(2) : ", matchObj.group(2))
else:
    print("Nothing found!!")

"""Python offers two different primitive operations based on regular expressions: match checks for a match 
only at the beginning of the string, while search checks for a match anywhere in the string"""

line = "Cats are smarter than dogs"

matchObj = re.match(r"dogs", line, re.M | re.I)
if matchObj:
    print("match --> matchObj.group() : ", matchObj.group())
else:
    print("No match!!")

searchObj = re.search(r"dogs", line, re.M | re.I)
if searchObj:
    print("search --> searchObj.group() : ", searchObj.group())
else:
    print("Nothing found!!")
