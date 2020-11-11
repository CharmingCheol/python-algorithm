import sys
from collections import deque

sys.setrecursionlimit(10 ** 6)

height, width = map(int, sys.stdin.readline().split())
board = [list(map(str, sys.stdin.readline().strip())) for _ in range(height)]
around = [[-1, 0], [0, 1], [1, 0], [0, -1]]
visited = [[0] * width for _ in range(height)]
visited[0][0] = 1
queue = deque()
queue.append([0, 0])

while queue:
    (now_y, now_x) = queue.popleft()
    for (around_y, around_x) in around:
        next_y = around_y + now_y
        next_x = around_x + now_x
        if 0 <= next_y < height and 0 <= next_x < width:
            if board[next_y][next_x] == "1":
                board[next_y][next_x] = "0"
                queue.append([next_y, next_x])
                visited[next_y][next_x] = visited[now_y][now_x] + 1
print(visited[height - 1][width - 1])