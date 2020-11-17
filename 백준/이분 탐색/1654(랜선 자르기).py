import sys

size, target = map(int, sys.stdin.readline().split())
nums = [int(sys.stdin.readline()) for _ in range(size)]
left = 1
right = max(nums)
while left <= right:
    mid = (left + right) // 2
    count = 0
    for num in nums:
        count += num // mid
    if count < target:
        right = mid - 1
    else:
        left = mid + 1
print(right)
