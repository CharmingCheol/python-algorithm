import sys

size = int(sys.stdin.readline())
table = []
for _ in range(size):
    table.append(list(map(int, sys.stdin.readline().split())))
table = sorted(table, key=lambda x: x[1])

current = table[0][1]
result = 1
for (start, end) in table:
    if current <= start:
        current = end
        result += 1
print(result)
