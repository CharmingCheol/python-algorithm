import sys
from collections import deque

size, limit = map(int, sys.stdin.readline().split())
nums = [item + 1 for item in range(size)]
deq = deque(nums)
count = 0
while len(deq) != 1:
    if count == limit - 1:
        deq.popleft()
        count = 0
    else:
        deq.append(deq.popleft())
        count += 1
print(deq[0])