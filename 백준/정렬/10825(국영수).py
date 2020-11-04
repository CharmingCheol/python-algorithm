import sys

size = int(sys.stdin.readline())
table = [list(map(str, sys.stdin.readline().split())) for _ in range(size)]
table.sort(key=lambda x: (-int(x[1]), int(x[2]), (-int(x[3])), x[0]))
for item in table:
    print(item[0])
