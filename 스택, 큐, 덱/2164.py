import sys

arr = [i + 1 for i in range(int(sys.stdin.readline()))]
while len(arr) != 1:
    arr.pop(0)
    add = arr.pop(0)
    arr.append(add)
print(*arr)