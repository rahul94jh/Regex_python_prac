import re

street = "N22, 2002, Jaypee Aman 2, Noida sec-152"
print(street)
street = re.sub(r"(\s+2,)", " 3,", street)
print(street)

searchObj = re.search(r"(\s3,)", street)
start = searchObj.start()
end = searchObj.end()

street = street[: start + 1] + "1," + street[end:]
print(street)
