import sys
import copy
from collections import deque

sys.stdin = open("input.txt")


def BFS():
    global result
    copyQueue = copy.copy(queue)
    count = 0
    while copyQueue:
        (now_y, now_x) = copyQueue.popleft()
        for (around_y, around_x) in around:
            next_y = now_y + around_y
            next_x = now_x + around_x
            if 0 <= next_y < N and 0 <= next_x < M:
                if board[next_y][next_x] == 0:
                    board[next_y][next_x] = 2
                    copyQueue.append([next_y, next_x])
    for y in range(N):
        for x in range(M):
            if board[y][x] == 0:
                count += 1
            elif board[y][x] == 2:
                board[y][x] = 0
    for (y, x) in queue:
        board[y][x] = 2
    result = max(result, count)


def DFS(count):
    if count == 3:
        BFS()
        return
    for a in range(N):
        for b in range(M):
            if board[a][b] == 0:
                board[a][b] = 1
                DFS(count + 1)
                board[a][b] = 0


N, M = map(int, sys.stdin.readline().split())
board = []
queue = deque()
for y in range(N):
    line = list(map(int, sys.stdin.readline().split()))
    board.append(line)
    for x in range(M):
        if line[x] == 2:
            queue.append([y, x])
around = [[-1, 0], [0, 1], [1, 0], [0, -1]]
result = 0
DFS(0)
print(result)
