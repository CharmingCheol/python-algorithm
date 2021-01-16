import sys
from collections import deque


def BFS():
    queue = deque([(0, 0)])
    visited[0][0] = -1
    while queue:
        now_y, now_x = queue.popleft()
        for around_y, around_x in around:
            next_y = now_y + around_y
            next_x = now_x + around_x
            if 0 <= next_y < height and 0 <= next_x < width:
                if board[now_y][now_x] == 0 and board[next_y][next_x] == 1:
                    visited[next_y][next_x] += 1
                elif board[now_y][now_x] == 0 and board[next_y][next_x] == 0 and visited[next_y][next_x] == 0:
                    visited[next_y][next_x] = -1
                    queue.append([next_y, next_x])


height, width = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(height)]
visited = [[0] * width for _ in range(height)]
around = [[-1, 0], [0, 1], [1, 0], [0, -1]]
result = 0

while True:
    BFS()
    twoMoreThan = 0
    for y in range(height):
        for x in range(width):
            if 2 <= visited[y][x]:
                board[y][x] = 0
                twoMoreThan += 1
            visited[y][x] = 0
    if twoMoreThan == 0: break
    result += 1
print(result)
