import re

text = "there are several festivals in india and almost all the months are festive months, \
Diwali and holi are two major festivals."

pattern = "festiv[a-z]+"
for match in re.finditer(pattern, text):
    print(match.group(), match.start(), match.end())

# find all the dates format
url = "http://www.telegraph.co.uk/formula-1/2017/10/28/mexican-grand-prix-2017-time-does-start-tv-channel-odds-lewisl/2017/05/12/"
pattern = r"/(\d{4})/(\d{1,2})/(\d{1,2})/"
print(re.findall(pattern, url))

"""Write a regular expression to extract all the words from a given sentence.
 Then use the re.finditer() function and store all the matched words that are of 
 length more than or equal to 5 letters in a separate list called result."""


string = "Do not compare apples with oranges. Compare apples with apples"

# regex pattern
pattern = r"(\w+)"

# store results in the list 'result'
result = []

# iterate over the matches
for match in re.finditer(
    pattern, string
):  # replace the ___ with the 'finditer' function to extract 'pattern' from the 'string'
    if len(match.group()) >= 5:
        result.append(match)
    else:
        continue

# evaluate result - don't change the following piece of code, it is used to evaluate your regex
print(len(result))

text = "Playing outdoor games when its raining outside is always fun!"

# regex pattern
pattern = r"(\w{0,}ing)"

# store results in the list 'result'
print(re.findall(pattern, text))
