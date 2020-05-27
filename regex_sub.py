import re

# http://acepor.github.io/2016/01/04/Backreference-python/

# Substtitute 2 between Aman & Noida with 1
street = "N22, 2002, Jaypee Aman 2, Noida sec-152"
print(street)
# street = re.sub(r"(\s+2,)", " 3,", street)
# print(street)

# searchObj = re.search(r"(\s3,)", street)
# start = searchObj.start()
# end = searchObj.end()

# street = street[: start + 1] + "1," + street[end:]
# print(street)

# unnamed capture group & backreferencing
p = re.compile(r"(\s+)\d{1}(,)")
print(p.sub(r"\g<1>1\g<2>", street))

# named capture group & backreferencing
p = re.compile(r"(?P<ss>\s+)\d(?P<dd>[,])")
print(p.sub(r"\g<ss>1\g<dd>", street))

# Using the non-capturing group to find the pattern,
# and substitute the whole pattern instead of using the backreference.
p = re.compile(r"(?:\s+)\d(?:[,])")
print(p.sub(" 1,", street))

"""replacement can also be a function, which gives you even more control. 
If replacement is a function, the function is called for every non-overlapping occurrence 
of pattern. On each call, the function is passed a match object argument for the match and can 
use this information to compute the desired replacement string and return it."""


def hexrepl(match):
    "Return the hex string for a decimal number"
    value = int(match.group())
    return hex(value)


p = re.compile(r"\d+")

print(p.sub(hexrepl, "Call 65490 for printing, 49152 for user code."))
