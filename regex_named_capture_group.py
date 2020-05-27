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
