import sys

size, target = map(int, sys.stdin.readline().split())
nums = [int(sys.stdin.readline()) for _ in range(size)]
nums.sort()

left = 1
right = nums[-1] - nums[0]
result = 0

while left <= right:
    mid = (left + right) // 2
    temp = nums[0]
    count = 1
    for num in nums[1:]:
        if mid < num - temp:
            count += 1
            temp = num
    if count < target:
        right = mid - 1
        result = mid
    else:
        left = mid + 1
print(result)