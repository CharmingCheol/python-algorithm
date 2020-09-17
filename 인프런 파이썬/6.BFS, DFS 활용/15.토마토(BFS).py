import sys
from _collections import deque

# 기준점 상하좌우 상대좌표
around = [[-1, 0], [0, 1], [1, 0], [0, -1]]

# 판자의 가로, 세로 크기
width, height = map(int, sys.stdin.readline().split())
board = []

day = [[0] * width for _ in range(height)]
queue = deque()
result = 0
flag = True

for y in range(height):
    line = list(map(int, sys.stdin.readline().split()))
    board.append(line)
    for x in range(width):
        if line[x] == 1:
            queue.append((y, x))

while queue:
    (now_y, now_x) = queue.popleft()
    for (around_y, around_x) in around:
        next_y = around_y + now_y
        next_x = around_x + now_x
        if 0 <= next_y < height and 0 <= next_x < width and board[next_y][next_x] == 0:
            queue.append((next_y, next_x))
            board[next_y][next_x] = 1
            day[next_y][next_x] = day[now_y][now_x] + 1
            result = day[next_y][next_x]

for y in range(height):
    for x in range(width):
        if board[y][x] == 0:
            flag = False
            break
print(result if flag else -1)
