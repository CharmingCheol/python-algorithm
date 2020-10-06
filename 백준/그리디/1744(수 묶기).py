import sys

size = int(sys.stdin.readline())
natural = []
negative = []
result = 0

for _ in range(size):
    num = int(sys.stdin.readline())
    if num <= 0:
        negative.append(num)
    elif num == 1:
        result += 1
    elif 1 < num:
        natural.append(num)

natural.sort(reverse=True)
negative.sort()

for index in range(0, len(natural), 2):
    if index == len(natural) - 1:
        result += natural[index]
    else:
        result += natural[index] * natural[index + 1]

for index in range(0, len(negative), 2):
    if index == len(negative) - 1:
        result += negative[index]
    else:
        result += negative[index] * negative[index + 1]
print(result)