import sys
from collections import deque


def BFS(start):
    queue = deque()
    queue.append(start)
    visited = [True] * (node + 1)
    visited[start] = False
    temp = 0
    while queue:
        now = queue.popleft()
        for i in board[now]:
            if visited[i]:
                visited[i] = False
                queue.append(i)
                temp += 1
    return temp


node, path = map(int, sys.stdin.readline().split())
board = [[] for _ in range(node + 1)]
result = [0] * (node + 1)
for _ in range(path):
    a, b = map(int, sys.stdin.readline().split())
    board[b].append(a)

for i in range(1, node + 1):
    result[i] = BFS(i)

max_value = max(result)
for index in range(1, node + 1):
    if max_value == result[index]:
        print(index, end=" ")
