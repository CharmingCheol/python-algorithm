import sys
from collections import deque

MAX_SIZE = 100001
start, end = map(int, sys.stdin.readline().split())
board = [float("inf")] * MAX_SIZE
board[start] = 0

queue = deque()
queue.append((start, 0))
while queue:
    now, value = queue.popleft()
    if now == end:
        print(board[now])
        break
    if value != board[now]: continue

    if 0 <= now - 1 and value + 1 < board[now - 1]:
        board[now - 1] = value + 1
        queue.append((now - 1, value + 1))
    if now + 1 < MAX_SIZE and value + 1 < board[now + 1]:
        board[now + 1] = value + 1
        queue.append((now + 1, value + 1))
    if now * 2 < MAX_SIZE and value < board[now * 2]:
        board[now * 2] = value
        queue.append((now * 2, value))
