import sys
size = int(sys.stdin.readline())
chart = []
for _ in range(size):
    chart.append(list(map(int, sys.stdin.readline().split())))
chart.sort(key=lambda x: -x[0])

current = chart[0][1]
result = size
for (height, weight) in chart[1:]:
    if current >= weight:
        result -= 1
    else:
        current = weight
print(result)