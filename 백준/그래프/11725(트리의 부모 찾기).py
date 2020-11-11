import sys
from collections import deque

sys.setrecursionlimit(10 ** 6)

size = int(sys.stdin.readline())
nums = [[] for _ in range(size + 1)]
queue = deque()
queue.append(1)
result = [0] * (size + 1)
check = [False] * (size + 1)

for _ in range(size - 1):
    (a, b) = map(int, sys.stdin.readline().split())
    nums[a].append(b)
    nums[b].append(a)
while queue:
    now = queue.popleft()
    for num in nums[now]:
        if not check[num]:
            result[num] = now
            queue.append(num)
            check[num] = True
for index in range(2, size + 1):
    print(result[index])
