import sys
from collections import deque

height, width = map(int, sys.stdin.readline().split())
board = [list(map(str, sys.stdin.readline().strip())) for _ in range(height)]
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
queue = deque()
result = 0

for y in range(height):
    for x in range(width):
        if board[y][x] == "L":
            visited = [[0] * width for _ in range(height)]
            visited[y][x] = 1
            queue.append([y, x])
            temp = 0
            while queue:
                now_y, now_x = queue.popleft()
                for i in range(4):
                    next_y = dy[i] + now_y
                    next_x = dx[i] + now_x
                    if 0 <= next_y < height and 0 <= next_x < width:
                        if board[next_y][next_x] == "L" and visited[next_y][next_x] == 0:
                            visited[next_y][next_x] = visited[now_y][now_x] + 1
                            queue.append([next_y, next_x])
                            temp = max(temp, visited[next_y][next_x] - 1)
            result = max(result, temp)
print(result)
