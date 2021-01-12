import sys
from collections import deque


def BFS(start):
    queue = deque([(start, 0)])
    visited = [True] * 10001
    while queue:
        now, level = queue.popleft()
        if now == end:
            return level
        NOW = str(now)
        for i in range(4):
            for j in map(str, range(10)):
                if i == 0 and j == "0":
                    continue
                num = int(NOW[:i] + j + NOW[i + 1:])
                if 1000 < num < 10000 and eratos[num] and visited[num]:
                    visited[num] = False
                    queue.append((num, level + 1))


eratos = [False] * 2 + [True] * 10000
for (index, num) in enumerate(eratos):
    if num:
        for trueIndex in range(2 * index, len(eratos), index):
            eratos[trueIndex] = False
for _ in range(int(sys.stdin.readline())):
    start, end = map(int, sys.stdin.readline().split())
    print(BFS(start))
