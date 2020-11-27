import sys


def DFS(y, x):
    for i in range(4):
        next_y = y + dy[i]
        next_x = x + dx[i]
        if 0 <= next_y < height and 0 <= next_x < width:
            if board[next_y][next_x] == 1:
                board[next_y][next_x] = 0
                DFS(next_y, next_x)


dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

for _ in range(int(sys.stdin.readline())):
    (width, height, cabbage) = map(int, sys.stdin.readline().split())
    board = [[0] * width for _ in range(height)]
    count = 0
    for _ in range(cabbage):
        (x, y) = map(int, sys.stdin.readline().split())
        board[y][x] = 1
    for y in range(height):
        for x in range(width):
            if board[y][x] == 1:
                count += 1
                board[y][x] = 0
                DFS(y, x)
    print(count)
