import sys
from collections import deque

size, limit = map(int, sys.stdin.readline().split())
nums = deque(list(map(int, sys.stdin.readline().split())))
index = deque(list(item for item in range(size)))
max_num = max(nums)
result = 0
while True:
    if nums[0] == max_num:
        if index[0] == limit:
            result += 1
            break
        nums.popleft()
        index.popleft()
        max_num = max(nums)
        result += 1
    else:
        nums.append(nums.popleft())
        index.append(index.popleft())
print(result)
