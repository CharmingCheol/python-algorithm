import sys

arr = []
for i in range(int(sys.stdin.readline())):
    arr.append(list(sys.stdin.readline().strip().split()))
arr.sort(key=lambda x: int(x[0]))
for i in arr:
    print(i[0], i[1])