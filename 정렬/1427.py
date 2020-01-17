import sys

num = list(map(int, str(sys.stdin.readline().strip())))
result = sorted(num, reverse=True)
for i in result:
    print(i, end="")
