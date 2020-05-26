import re


def find_pattern(text, patterns):
    if re.search(patterns, text):
        return re.search(patterns, text)
    else:
        return "No Match Found!"


print(
    find_pattern("aabbbbbb", "ab{3,5}")
)  # return if a is followed by b 3-5 times GREEDY

print(
    find_pattern("aabbbbbb", "ab{3,5}?")
)  # return if a is followed by b 3-5 times Non GREEDY

print(find_pattern("<html><title>This is a title</title</html>", "<.*>"))  # GREEDY

print(find_pattern("<html><title>This is a title</title</html>", "<.*?>"))  # NON GREEDY
