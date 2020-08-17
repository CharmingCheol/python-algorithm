import sys

size, require = map(int, sys.stdin.readline().split())
num_list = list(map(int, sys.stdin.readline().split()))

left = 0
right = sum(num_list)
result = 0

while left < right:
    middle = (left + right) // 2
    count = 1
    total = 0
    for item in num_list:
        total += item
        if total >= middle:
            count += 1
            total = item
    if count > require:
        left = middle + 1
    else:
        right = middle
        result = middle - 1
print(result)
