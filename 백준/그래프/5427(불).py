import sys
from collections import deque

around = [[-1, 0], [0, 1], [1, 0], [0, -1]]


def BFS(start, fire_board):
    queue = deque([start])
    board[start[0]][start[1]] = 0
    while queue:
        now_y, now_x = queue.popleft()
        for around_y, around_x in around:
            next_y = around_y + now_y
            next_x = around_x + now_x
            if next_x == -1:
                return board[now_y][now_x] + 1
            elif next_x == width:
                return board[now_y][now_x] + 1
            elif next_y == -1:
                return board[now_y][now_x] + 1
            elif next_y == height:
                return board[now_y][now_x] + 1
            if board[next_y][next_x] == "." and board[now_y][now_x] + 1 < fire_board[next_y][next_x]:
                board[next_y][next_x] = board[now_y][now_x] + 1
                queue.append([next_y, next_x])
    return "IMPOSSIBLE"


for _ in range(int(sys.stdin.readline())):
    width, height = map(int, sys.stdin.readline().split())
    board = []
    fire = deque()
    fire_board = [[float("inf")] * width for _ in range(height)]
    start = []
    for y in range(height):
        line = list(map(str, sys.stdin.readline().strip()))
        for x in range(width):
            if line[x] == "*":
                fire.append([y, x])
                fire_board[y][x] = 0
            elif line[x] == "@":
                start = [y, x]
        board.append(line)
    while fire:
        now_y, now_x = fire.popleft()
        for around_y, around_x in around:
            next_y = around_y + now_y
            next_x = around_x + now_x
            if 0 <= next_y < height and 0 <= next_x < width and fire_board[next_y][next_x] == float("inf"):
                if board[next_y][next_x] == "." or board[next_y][next_x] == "@":
                    fire.append([next_y, next_x])
                    fire_board[next_y][next_x] = fire_board[now_y][now_x] + 1
    print(BFS(start, fire_board))
