import sys
from collections import deque


def BFS(y, x, color, board):
    queue = deque([(y, x)])
    board[y][y] = 0
    while queue:
        now_y, now_x = queue.popleft()
        for around_y, around_x in around:
            next_y = around_y + now_y
            next_x = around_x + now_x
            if 0 <= next_y < size and 0 <= next_x < size:
                if board[next_y][next_x] and color == board[next_y][next_x]:
                    board[next_y][next_x] = 0
                    queue.append((next_y, next_x))


size = int(sys.stdin.readline())
board1 = []
board2 = []
around = [[-1, 0], [0, 1], [1, 0], [0, -1]]
result1 = 0
result2 = 0

for _ in range(size):
    line = list(map(str, sys.stdin.readline().strip()))
    board1.append(line)
    temp = []
    for item in line:
        if item == "R" or item == "G":
            temp.append("R")
        else:
            temp.append("B")
    board2.append(temp)

for y in range(size):
    for x in range(size):
        if board1[y][x]:
            BFS(y, x, board1[y][x], board1)
            result1 += 1
        if board2[y][x]:
            BFS(y, x, board2[y][x], board2)
            result2 += 1
print(result1, result2)
