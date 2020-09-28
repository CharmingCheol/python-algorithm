import sys

size = int(sys.stdin.readline())

nums = [0] * (size + 1)
nums[1] = 1
nums[2] = 2

for index in range(3, size + 1):
    nums[index] = nums[index - 2] + nums[index - 1]
