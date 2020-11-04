import sys

size = int(sys.stdin.readline())
temp = dict()
for _ in range(size):
    num = int(sys.stdin.readline())
    if num in temp:
        temp[num] += 1
    else:
        temp[num] = 1
temp = sorted(temp.items(), key=lambda x: (-x[1], x[0]))
print(temp[0][0])
