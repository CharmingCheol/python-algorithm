import sys
from collections import deque

input = sys.stdin.readline


def rotate_180(y, x, dir):
    if dir == 0:
        temp = 1
    elif dir == 1:
        temp = 0
    elif dir == 2:
        temp = 3
    else:
        temp = 2
    if visited[y][x][temp] == -1:
        visited[y][x][temp] = visited[y][x][dir] + 2
        queue.append([y, x, temp])


def rotate_R(y, x, dir):
    if dir == 0:
        temp = 2
    elif dir == 1:
        temp = 3
    elif dir == 2:
        temp = 1
    else:
        temp = 0
    if visited[y][x][temp] == -1:
        visited[y][x][temp] = visited[y][x][dir] + 1
        queue.append([y, x, temp])


def rotate_L(y, x, dir):
    if dir == 0:
        temp = 3
    elif dir == 1:
        temp = 2
    elif dir == 2:
        temp = 0
    else:
        temp = 1
    if visited[y][x][temp] == -1:
        visited[y][x][temp] = visited[y][x][dir] + 1
        queue.append([y, x, temp])


def BFS():
    queue.append([sy - 1, sx - 1, sd - 1])
    visited[sy - 1][sx - 1][sd - 1] = 0
    while queue:
        now_y, now_x, now_dir = queue.popleft()
        if now_y == ey - 1 and now_x == ex - 1 and now_dir == ed - 1:
            print(visited[now_y][now_x][now_dir])
            return
        ny, nx = now_y, now_x
        for i in range(3):
            ny += around[now_dir][0]
            nx += around[now_dir][1]
            if 0 <= ny < height and 0 <= nx < width:
                if board[ny][nx] == 0:
                    if visited[ny][nx][now_dir] == -1:
                        visited[ny][nx][now_dir] = visited[now_y][now_x][now_dir] + 1
                        queue.append([ny, nx, now_dir])
                else:
                    break
        rotate_R(now_y, now_x, now_dir)
        rotate_L(now_y, now_x, now_dir)
        rotate_180(now_y, now_x, now_dir)


height, width = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(height)]
sy, sx, sd = list(map(int, input().split()))
ey, ex, ed = list(map(int, input().split()))

visited = [[[-1] * 4 for _ in range(width)] for _ in range(height)]
queue = deque()
around = [[0, 1], [0, -1], [1, 0], [-1, 0]]
BFS()
