import re

# ?p<group_name> :- named capture group
p = re.compile(r"(?P<word>\b\w+\b)")
m = p.search("(((( Lots of punctuation)))")

print(m.group("word"))

m = re.match(r"(?P<first>\w+) (?P<last>\w+)", "Jane Doe")
print(m.groupdict())

# EXtract different parts of the email
m = re.match(
    r"(?P<username>\b\w+\b)[@](?P<domain>\b[a-z]{3,5}\b)[.](?P<ext>\b[a-z]{2,3}\b)",
    "ramaya47mh@gmail.com",
)
print(m.groupdict())
print(m.group("username"))
print(m.group("domain"))
print(m.group("ext"))


# Example usage of findall(). In the given URL find all dates
url = "http://www.telegraph.co.uk/formula-1/2017/10/28/mexican-grand-prix-2017-time-does-start-tv-channel-odds-lewisl/2017/05/12/"

# named capture group
date_regex = re.compile(r"/(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})/")

print(date_regex.findall(url))  # find all matches

result = date_regex.search(url)  # get the first match for the groups defined
print("Year: ", result.group("year"))  # fetch the year group first match from search
print("Month: ", result.group("month"))  # fetch the year group first match from search
print("Day: ", result.group("day"))  # fetch the year group first match from search


"""You have a string which contains a data in the format DD-MM-YYYY.
 Write a regular expression to extract the date from the string."""

string = "Today’s date is 18-05-2018."

# regex pattern - we can use named capture group here as well
pattern = r"(\d{1,2})-(\d{1,2})-(\d{4})"

# store result
result = re.search(pattern, string)

print(result)

"""use grouping to extract the month from the date. The expected date format is DD-MM-YYYY only."""

string = "Today's date is 18-05-2018"

# regex pattern
pattern = r"(?P<day>\d{1,2})-(?P<month>\d{1,2})-(?P<year>\d{4})"
# store result
result = re.search(pattern, string)
# extract month using group command
if result != None:
    month = result.group("month")
else:
    month = "NA"
# evaluate result - don't change the following piece of code, it is used to evaluate your regex
print(month)


"""Write a regular expression to extract the domain name from an email address. 
The format of the email is simple - the part before the ‘@’ symbol contains alphabets, 
numbers and underscores. The part after the ‘@’ symbol contains only alphabets followed by a dot followed by ‘com’"""

string = "user_name_123@gmail.com"
# regex pattern
pattern = r"(?P<domain>\b[a-z]{4,6}[.][a-z]{3}\b)"
# store result
result = re.search(pattern, string)
# extract domain using group command
if result != None:
    domain = result.group("domain")
else:
    domain = "NA"
print(domain)
