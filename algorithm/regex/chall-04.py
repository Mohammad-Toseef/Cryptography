import re

item = "hello 123 45 7898 hi"
obj = re.match(r"([0-9]+( [0-9]+)+)*.([0-9]+(-[0-9]+)+)*.[0-9]+", item)
print(obj.group())
