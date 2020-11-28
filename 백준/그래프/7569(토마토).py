import sys
from collections import deque

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

width, depth, height = map(int, sys.stdin.readline().split())
queue = deque()
board = []
flag = True
result = 0
for y in range(depth * height):
    line = list(map(int, sys.stdin.readline().split()))
    board.append(line)
    for (x, item) in enumerate(line):
        if line[x] == 1:
            level = y // depth if 0 <= y // depth else 0
            queue.append([y, x, 0, level])
while queue:
    now_y, now_x, day, level = queue.popleft()
    for i in range(4):
        next_y = now_y + dy[i]
        next_x = now_x + dx[i]
        if level * depth <= next_y <= (level + 1) * depth - 1 and 0 <= next_x < width:
            if board[next_y][next_x] == 0:
                board[next_y][next_x] = 1
                queue.append([next_y, next_x, day + 1, level])
                result = max(result, day + 1)
    up_y = now_y - depth
    down_y = now_y + depth
    if 0 <= up_y and board[up_y][now_x] == 0:
        board[up_y][now_x] = 1
        queue.append([up_y, now_x, day + 1, level - 1])
        result = max(result, day + 1)
    if down_y < depth * height and board[down_y][now_x] == 0:
        board[down_y][now_x] = 1
        queue.append([down_y, now_x, day + 1, level + 1])
        result = max(result, day + 1)

for y in range(depth * height):
    for x in range(width):
        if board[y][x] == 0:
            flag = False
            break
    if not flag:
        break
print(result if flag else -1)
