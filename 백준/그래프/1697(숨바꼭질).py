import sys
from collections import deque

sys.stdin = open("input.txt")
sys.setrecursionlimit(10 ** 6)

subin, brother = map(int, sys.stdin.readline().split())
visited = [False] * 100001
count = 0
queue = deque([[subin, count]])

while queue:
    now = queue.popleft()
    coord = now[0]
    count = now[1]
    if not visited[coord]:
        visited[coord] = True
        if coord == brother:
            print(count)
            break
        count += 1
        if (coord * 2) <= 100000:
            queue.append([coord * 2, count])
        if (coord + 1) <= 100000:
            queue.append([coord + 1, count])
        if 0 <= (coord - 1):
            queue.append([coord - 1, count])
