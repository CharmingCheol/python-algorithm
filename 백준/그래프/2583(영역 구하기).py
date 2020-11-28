import sys
from collections import deque

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

height, width, block = map(int, sys.stdin.readline().split())
board = [[0] * width for _ in range(height)]
queue = deque()
result = []
for _ in range(block):
    start_x, start_y, end_x, end_y = map(int, sys.stdin.readline().split())
    for y in range(start_y, end_y):
        for x in range(start_x, end_x):
            board[y][x] = 1
for y in range(height):
    for x in range(width):
        if board[y][x] == 0:
            board[y][x] = 1
            count = 1
            queue.append([y, x])
            while queue:
                now_y, now_x = queue.popleft()
                for i in range(4):
                    next_y = dy[i] + now_y
                    next_x = dx[i] + now_x
                    if 0 <= next_y < height and 0 <= next_x < width and board[next_y][next_x] == 0:
                        count += 1
                        board[next_y][next_x] = 1
                        queue.append([next_y, next_x])
            result.append(count)

result.sort()
print(len(result))
for item in result:
    print(item, end=" ")
