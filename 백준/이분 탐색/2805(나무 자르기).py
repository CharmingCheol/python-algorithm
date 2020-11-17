import sys

size, target = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))
left = 1
right = max(nums)
while left <= right:
    mid = (left + right) // 2
    count = 0
    for num in nums:
        if 0 < num - mid:
            count += num - mid
        if target <= count:
            left = mid + 1
            break
    else:
        right = mid - 1
print(right)
