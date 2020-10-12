import sys

size = int(sys.stdin.readline())
seats = list(map(str, sys.stdin.readline()))
L_count = 0
result = 1

for seat in seats:
    if seat == "S":
        result += 1
    elif seat == "L":
        L_count += 1
        if L_count == 2:
            result += 1
            L_count = 0
if size < result:
    print(size)
else:
    print(result)