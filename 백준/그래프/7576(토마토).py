import sys
from _collections import deque

sys.setrecursionlimit(10 ** 6)

width, height = map(int, sys.stdin.readline().split())
board = []
queue = deque()
around = [[-1, 0], [0, 1], [1, 0], [0, -1]]
level = [[0] * width for _ in range(height)]
day = 0
flag = True
for y in range(height):
    line = list(map(int, sys.stdin.readline().split()))
    board.append(line)
    for x in range(width):
        if line[x] == 1:
            queue.append([y, x])
while queue:
    (now_y, now_x) = queue.popleft()
    for (around_y, around_x) in around:
        next_y = around_y + now_y
        next_x = around_x + now_x
        if 0 <= next_y < height and 0 <= next_x < width:
            if board[next_y][next_x] == 0:
                board[next_y][next_x] = 1
                level[next_y][next_x] = level[now_y][now_x] + 1
                day = level[next_y][next_x]
                queue.append([next_y, next_x])
for y in range(height):
    for x in range(width):
        if board[y][x] == 0:
            flag = False
            break
print(day if flag else -1)
