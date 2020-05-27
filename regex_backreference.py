import re

"""Backreferences in a pattern allow you to specify that the contents of an earlier capturing 
group must also be found at the current location in the string. For example,
 \1 will succeed if the exact contents of group 1 can be found at the current position, 
 and fails otherwise. Remember that Python’s string literals also use a backslash followed by 
 numbers to allow including arbitrary characters in a string, so be sure to use a raw string when
  incorporating backreferences in a RE."""


""" Replace oo between z & t with 00 """
tt = "zootoozootoo"

# 1> Using unnamed captured group for backreferencing
O_ZERO = re.compile(r"(z)oo(t)")
print(O_ZERO.sub(r"\g<1>00\g<2>", tt))

# 2> Using named captured group or backreferencing
O_ZERO = re.compile(r"(?P<ZZ>z)oo(?P<TT>t)")
print(O_ZERO.sub(r"\g<ZZ>00\g<TT>", tt))

# 3> Using the non-capturing group to find the pattern,
# and substitute the whole pattern instead of using the backreference.
O_ZERO = re.compile("(?:z)oo(?:t)")
print(O_ZERO.sub("z00t", tt))
