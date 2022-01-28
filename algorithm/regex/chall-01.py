import re

regex = "([0-9a-f]{1,4}:){7}([0-9a-f]){1,4}"

Ip = "hi2001:0db8:0000:0000:0000:8a2e:0370:7334hello"
if (re.search(regex, Ip)):
    search = re.search(regex, Ip)
    print(search.group())

else:
    print("No valid ipv6 address found in string")