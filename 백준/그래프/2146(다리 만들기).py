import sys
from collections import deque

sys.setrecursionlimit(10 ** 6)


def DFS(y, x, island_number):
    for (around_y, around_x) in around:
        next_y = around_y + y
        next_x = around_x + x
        if 0 <= next_y < size and 0 <= next_x < size:
            if board[next_y][next_x] == 1:
                board[next_y][next_x] = island_number
                DFS(next_y, next_x, island_number)
            if board[next_y][next_x] == 0:
                queue.append([next_y, next_x])
                indexed.append([y, x])
                level[next_y][next_x] = 1


size = int(sys.stdin.readline())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(size)]
level = [[0] * size for _ in range(size)]
around = [[-1, 0], [0, 1], [1, 0], [0, -1]]
island_number = 2
queue = deque()
indexed = deque()
result = 2164000000

for y in range(size):
    for x in range(size):
        if board[y][x] == 1:
            board[y][x] = island_number
            DFS(y, x, island_number)
            island_number += 1

while queue:
    (now_y, now_x) = queue.popleft()
    for (around_y, around_x) in around:
        next_y = around_y + now_y
        next_x = around_x + now_x
        if 0 <= next_y < size and 0 <= next_x < size:
            if board[next_y][next_x] == 0 and level[next_y][next_x] == 0:
                level[next_y][next_x] = level[now_y][now_x] + 1
                queue.append([next_y, next_x])
while indexed:
    (now_y, now_x) = indexed.popleft()
    for (around_y, around_x) in around:
        next_y = around_y + now_y
        next_x = around_x + now_x
        if 0 <= next_y < size and 0 <= next_x < size:
            if board[next_y][next_x] == 0:
                board[next_y][next_x] = board[now_y][now_x]
                indexed.append([next_y, next_x])
            elif board[next_y][next_x] != board[now_y][now_x]:
                temp = level[next_y][next_x] + level[now_y][now_x]
                result = temp if temp < result else result
print(result)