import sys
from collections import deque


def BFS():
    queue = deque([(0, 0)])
    visited = [[True] * width for _ in range(height)]
    while queue:
        now_y, now_x = queue.popleft()
        for around_y, around_x in around:
            next_y = now_y + around_y
            next_x = now_x + around_x
            if 0 <= next_y < height and 0 <= next_x < width:
                if board[next_y][next_x] == 1:
                    board[next_y][next_x] = -1
                elif board[next_y][next_x] == 0 and visited[next_y][next_x] == True:
                    visited[next_y][next_x] = False
                    queue.append((next_y, next_x))

height, width = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(height)]
around = [[-1, 0], [0, 1], [1, 0], [0, -1]]
hour = 0
count = 0
while True:
    temp = 0
    BFS()
    for y in range(height):
        for x in range(width):
            if board[y][x] == -1:
                temp += 1
                board[y][x] = 0
    if temp == 0: break
    hour += 1
    count = temp
print(hour)
print(count)
