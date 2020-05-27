import re

""" Extract valid mail id's from given text
 - first char must be an alphabet
 - the min length of username is 3 and max is 15
 - min domain length should be 3 and max 10 (alphabets only)
 - ext should contain min 2 or max 3  (alphabets only) """

regex = r"\b[a-z]\w{2,15}[@][a-z]{3,10}[.][a-z]{2,3}\b"

test_str = "this is test text with few email id's like rahul1994jh@gmail.com, our job is to find \
    all emails like  abc@capitaliq.in, the pattern should be able to identify mail id's such as \
    Vikas_23@yahoo.com, we are not intrested in fetching malformed id's \
    like _arav222@test.in or #rahul1994kr@orkut.in, let's see if we can extract valid \
    email id's using regex or not?"

### Below code is automatically generated from the code generator provided at below url
### https://regex101.com/tests/codegen?language=python


matches = re.finditer(regex, test_str, flags=re.MULTILINE | re.IGNORECASE)

for matchNum, match in enumerate(matches, start=1):

    print(
        "Match {matchNum} was found at {start}-{end}: {match}".format(
            matchNum=matchNum, start=match.start(), end=match.end(), match=match.group()
        )
    )
