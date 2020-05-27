import re

"""" Create a pattern to extract the topic from the url """

regex = r"https?://[\w.]+/([\w-]+)"

test_str = (
    "https://times.co.in/PM-strikes-back\n"
    "http://nyc.com/heatwaves-striking-northern-India\n"
    "https://www.deccanherald.com/rahul-gandhi-trying-to-weaken-countrys-resolve-against-coronavirus-bjp-842485\n"
)

# Using findall
matches = re.findall(regex, test_str, re.MULTILINE)
# print all the topics from supplied url's
print(matches)

# Using finditer
matches = re.finditer(regex, test_str, re.MULTILINE)
for matchNum, match in enumerate(matches, start=1):

    print(
        "Match {matchNum} was found at {start}-{end}: {match}".format(
            matchNum=matchNum, start=match.start(), end=match.end(), match=match.group()
        )
    )
    for groupNum in range(0, len(match.groups())):
        groupNum = groupNum + 1
        print(
            "Topic found at {start}-{end}: {group}".format(
                start=match.start(groupNum),
                end=match.end(groupNum),
                group=match.group(groupNum),
            )
        )
