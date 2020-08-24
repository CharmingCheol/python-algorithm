import sys

stick = list(str(sys.stdin.readline()))
left = 0
right = 0
result = 0
for first in range(len(stick)):
    past = ""
    laser = 0
    for second in range(first, len(stick)):
        if stick[second] == "(":
            left += 1
        elif stick[second] == ")":
            right += 1
        if left == 1 and right == 1:
            break
        elif left < right:
            break
        elif left == right and laser != 0:
            result += laser + 1
            break
        if past == "(" and stick[second] == ")":
            laser += 1
        past = stick[second]
    left = 0
    right = 0
print(result)
