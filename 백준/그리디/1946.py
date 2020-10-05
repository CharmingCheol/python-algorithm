import sys

for _ in range(int(sys.stdin.readline())):
    size = int(sys.stdin.readline())
    nums = [list(map(int, sys.stdin.readline().split())) for _ in range(size)]
    nums = sorted(nums, key=lambda x: x[0])
    temp = nums[0][1]
    count = 0
    for index in range(1, size):
        if temp < nums[index][1]:
            count += 1
        else:
            temp = nums[index][1]
    print(size - count)
