import sys

arr = []
for i in range(int(sys.stdin.readline().strip())):
    arr.append(str(sys.stdin.readline().strip()))
result = list(set(arr))
result.sort(key=lambda x: (len(x), x))
for i in result:
    print(i)