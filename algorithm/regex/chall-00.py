import re
regex =  "(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)"
Ip = "hey255.1.2.2hello"
if (re.search(regex, Ip)):
    search = re.search(regex, Ip)
    print(search.group())

else:
    print("No valid Ipv4 address found in string")