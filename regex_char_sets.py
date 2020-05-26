import re


def find_pattern(text, patterns):
    if re.search(patterns, text):
        return re.search(patterns, text)
    else:
        return "No Match!"


# [' and ']'.
# They're used for specifying a character class, which is a set of characters that you wish to match.
# Characters can be listed individually as follows

print(find_pattern("a", "[abc]"))  # match
# Or a range of characters can be indicated by giving two characters and separating them by a '-'.
print(find_pattern("b", "[a-c]"))  # match
print(find_pattern("d", "[a-c]"))  # no match
