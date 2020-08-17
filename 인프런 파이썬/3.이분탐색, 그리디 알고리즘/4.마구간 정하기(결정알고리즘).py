import sys

size, require = map(int, sys.stdin.readline().split())
num_list = []
for _ in range(size):
    num_list.append(int(sys.stdin.readline()))
num_list.sort()

# 1 2 4 8 9
left = 1
right = max(num_list)
result = 0
while left <= right:
    middle = (left + right) // 2
    current = num_list[0]
    count = 1
    for index in range(1, size):
        if num_list[index] - current > middle:
            count += 1
            current = num_list[index]
    if count < require:
        right = middle - 1
        result = middle
    else:
        left = middle + 1
print(result)
