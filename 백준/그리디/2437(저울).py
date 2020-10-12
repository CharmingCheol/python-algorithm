import sys

size = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
nums.sort()
result = 0

for num in nums:
    if num - 1 <= result:
        result += num
    else:
        break
result += 1
print(result)