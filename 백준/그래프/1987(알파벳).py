import sys

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]


def BFS(y, x):
    global result
    queue = {(x, y, board[x][y])}
    while queue:
        now_y, now_x, path = queue.pop()
        for i in range(4):
            next_y = now_y + dy[i]
            next_x = now_x + dx[i]
            if 0 <= next_x < width and 0 <= next_y < height and board[next_y][next_x] not in path:
                queue.add((next_y, next_x, path + board[next_y][next_x]))
                result = max(result, len(path) + 1)


height, width = map(int, sys.stdin.readline().split())
board = [list(map(str, sys.stdin.readline().strip())) for _ in range(height)]
result = 1
BFS(0, 0)
print(result)