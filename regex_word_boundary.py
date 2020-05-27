import re

# \b :- Word boundary.
"""This is a zero-width assertion that matches only at the beginning or end of a word.
 A word is defined as a sequence of alphanumeric characters,
 so the end of a word is indicated by whitespace or a non-alphanumeric character."""

p = re.compile(r"\bclass\b")
text_1 = "I am from the class of 2011"
text_2 = "These are highly classified documents"
print(p.search(text_1))  # match
print(p.search(text_2))  # no match


""" Match the words which have min 3 and max 5 b in the middle of the word, 
i.e word shouldn't start and end with b"""

p = re.compile(r"\b[^(b\s+)]{1,}b{3,5}[^b]{1,}\b")
print(p.search("llbbbbbnnnn"))  # match
print(p.search("abbbdd"))  # match
print(p.search("abbbbbbc"))  # no match
print(p.search("mmbbc"))  # no match

text = "hibba mumbbbbbaaassa dibbbrugarh namabbbbbbbbbbii bbbittu  asambbbbhab nambbbb"
print(p.findall(text))
