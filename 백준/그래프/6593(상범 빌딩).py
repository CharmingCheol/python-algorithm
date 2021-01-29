import sys
from collections import deque

df = [1, -1, 0, 0, 0, 0]  # 층
dy = [0, 0, 1, -1, 0, 0]  # 세로
dx = [0, 0, 0, 0, 1, -1]  # 가로


def BFS():
    start_f, start_y, start_x = start
    visited = [[[0] * width for _ in range(height)] for _ in range(floor)]
    queue = deque()
    queue.append([start_f, start_y, start_x])
    while queue:
        now_floor, now_y, now_x = queue.popleft()
        for i in range(6):
            nf = now_floor + df[i]
            ny = now_y + dy[i]
            nx = now_x + dx[i]
            if 0 <= nf < floor and 0 <= ny < height and 0 <= nx < width:
                if board[nf][ny][nx] == "E":
                    dest = visited[now_floor][now_y][now_x] + 1
                    return "Escaped in " + str(dest) + " minute(s)."
                if board[nf][ny][nx] == "." and visited[nf][ny][nx] == 0:
                    visited[nf][ny][nx] = visited[now_floor][now_y][now_x] + 1
                    queue.append([nf, ny, nx])
    return "Trapped!"


while True:
    floor, height, width = map(int, sys.stdin.readline().split())
    if floor == height == width == 0: break
    board = []
    start = []
    for f in range(floor):
        temp = []
        for y in range(height):
            line = list(map(str, sys.stdin.readline().strip()))
            temp.append(line)
            for x in range(width):
                if line[x] == "S":
                    start = [f, y, x]
        board.append(temp)
        str(sys.stdin.readline())
    print(BFS())