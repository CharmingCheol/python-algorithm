import sys

size = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))

result = [0] * size
for first in range(size):
    for second in range(size):
        if nums[first] == 0 and result[second] == 0:
            result[second] = first + 1
            break
        elif result[second] == 0:
            nums[first] -= 1
for item in result:
    print(item, end=" ")