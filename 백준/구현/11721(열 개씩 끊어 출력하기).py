import sys

line = str(sys.stdin.readline())

result = []
temp = ""
for (index, char) in enumerate(line):
    temp += char
    if (index + 1) % 10 == 0:
        result.append(temp)
        temp = ""
if temp != "":
    result.append(temp)
for item in result:
    print(item)
