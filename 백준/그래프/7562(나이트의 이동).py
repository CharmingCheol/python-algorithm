import sys
from collections import deque

sys.stdin = open("input.txt")
sys.setrecursionlimit(10 ** 6)

dx = [-1, 1, 2, 2, 1, -1, -2, -2]
dy = [-2, -2, -1, 1, 2, 2, 1, -1]

for _ in range(int(sys.stdin.readline())):
    size = int(sys.stdin.readline())
    (start_y, start_x) = map(int, sys.stdin.readline().split())
    (end_y, end_x) = map(int, sys.stdin.readline().split())

    board = [[0] * size for _ in range(size)]
    board[start_y][start_x] = 1

    queue = deque([[start_y, start_x]])
    flag = True
    if start_y == end_y and start_x == end_x:
        print(0)
    else:
        while queue:
            if not flag:
                break
            now_y, now_x = queue.popleft()
            for i in range(8):
                next_y = now_y + dy[i]
                next_x = now_x + dx[i]
                if next_y == end_y and next_x == end_x:
                    print(board[now_y][now_x])
                    flag = False
                    break
                if 0 <= next_y < size and 0 <= next_x < size:
                    if board[next_y][next_x] == 0:
                        board[next_y][next_x] = board[now_y][now_x] + 1
                        queue.append([next_y, next_x])
