import sys

sys.setrecursionlimit(10 ** 6)


def DFS(y, x):
    for (around_y, around_x) in around:
        next_y = around_y + y
        next_x = around_x + x
        if 0 <= next_y < height and 0 <= next_x < width:
            if board[next_y][next_x] == "1":
                board[next_y][next_x] = "0"
                DFS(next_y, next_x)


while True:
    width, height = map(int, sys.stdin.readline().split())
    if width == 0 and height == 0:
        break
    board = [list(map(str, sys.stdin.readline().split())) for _ in range(height)]
    around = [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]
    count = 0
    for y in range(height):
        for x in range(width):
            if board[y][x] == "1":
                board[y][x] = "0"
                count += 1
                DFS(y, x)
    print(count)
