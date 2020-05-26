import re


def find_pattern(text, patterns):
    if re.search(patterns, text):
        return re.search(patterns, text)
    else:
        return "No Match Found!"


# [' and ']'.
# They're used for specifying a character class, which is a set of characters that you wish to match.
# Characters can be listed individually as follows

print(find_pattern("a", "[abc]"))  # match
# Or a range of characters can be indicated by giving two characters and separating them by a '-'.
print(find_pattern("b", "[a-c]"))  # match
print(find_pattern("d", "[a-c]"))  # no match

# \s :- [ \t\n\r\f\v]
# \S :- [^ \t\n\r\f\v]
print(find_pattern("rahul kumar", r"[a-z\s]+"))  # matches full name
print(find_pattern("rahul kumar", r"[a-z\S]+"))  # matches only first name

# \d :- [0-9]
# \D : [^0-9]
print(find_pattern("123Rahul", r"\d+"))  # match only digit
print(find_pattern("123@Rahul", r"\D+"))  # match non digits

# \w :- [a-zA-Z0-9_]
# \W :- [^a-zA-Z0-9_]
print(find_pattern("123_Rahul@jh.com", r"\w+"))  # match alphanumeric
print(find_pattern("123_Rahul@jh.com", r"\W+"))  # match non alphanumeric


# create a pattern for matching up the email
email_pattern = r"^[a-z]+\w+@{1}[a-z]{4,10}([.]{1}[a-z]{2,3})$"

print(find_pattern("rahul_kumar_jha@spglobal.in", email_pattern))  # match

print(find_pattern("19_rahul_kumar_jha@spglobal.in", email_pattern))  # no match

print(find_pattern("rahul_kumar_jha@au.in", email_pattern))  # no match

print(find_pattern("rahul_kumar_jha@spglobal", email_pattern))  # no match

print(find_pattern("rahul kumar_jha@spglobal", email_pattern))  # no match
