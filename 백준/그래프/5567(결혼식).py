import sys
from collections import deque

node = int(sys.stdin.readline())
path = int(sys.stdin.readline())
board = [[0] * (node + 1) for _ in range(node + 1)]
visited = [True] * (node + 1)
result = 0
for _ in range(path):
    y, x = map(int, sys.stdin.readline().split())
    board[y][x] = 1
    board[x][y] = 1

queue = deque([(1, 0)])
visited[1] = False
while queue:
    y, level = queue.popleft()
    for x in range(node + 1):
        if board[y][x] == 1 and visited[x]:
            print(y, x, level + 1)
            if level + 1 < 2:
                queue.append((x, level + 1))
            visited[x] = False
            result += 1
print(result)
