import sys

string = list(map(str, sys.stdin.readline().strip()))
temp = []
score = 0
for (index, item) in enumerate(string):
    if item == "(":
        temp.append("(")
    elif item == ")" and string[index - 1] == "(":
        temp.pop()
        score += len(temp)
    else:
        temp.pop()
        score += 1
print(score)
