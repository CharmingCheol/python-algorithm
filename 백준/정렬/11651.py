import sys

arr = []
for _ in range(int(sys.stdin.readline())):
    arr.append(list(map(int, sys.stdin.readline().strip().split())))
arr.sort(key=lambda x: (x[1], x[0]))
for i in arr:
    print(i[0], i[1])