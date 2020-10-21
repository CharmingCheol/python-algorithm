import sys

m = int(sys.stdin.readline())
n = int(sys.stdin.readline())
index = 1
total = []

while index ** 2 <= n:
    if m <= index ** 2 <= n:
        total.append(index ** 2)
    index += 1
if not total:
    print(-1)
else:
    print(sum(total))
    print(total[0])