import sys

first = sorted(str(sys.stdin.readline().strip()))
second = sorted(str(sys.stdin.readline().strip()))

if first != second:
    print("NO")
else:
    print("YES")
