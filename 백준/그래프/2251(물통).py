import sys
from collections import deque

A, B, C = map(int, sys.stdin.readline().split())
queue = deque()
queue.append([0, 0, C])
visited = [[True] * 201 for _ in range(201)]
result = [0] * 201

while queue:
    a, b, c = queue.popleft()

    if not visited[a][b]: continue
    if a == 0: result[c] = 1
    visited[a][b] = False

    # a -> b
    if a + b < B:
        queue.append([0, a + b, c])
    else:
        queue.append([a + b - B, B, c])

    # a -> c
    if a + c < C:
        queue.append([0, b, a + c])
    else:
        queue.append([a + c - C, b, C])

    # b -> a
    if b + a < A:
        queue.append([a + b, 0, c])
    else:
        queue.append([A, b + a - A, c])

    # b -> c
    if b + c < C:
        queue.append([a, 0, b + c])
    else:
        queue.append([a, b + c - C, C])

    # c -> a
    if a + c < A:
        queue.append([a + c, b, 0])
    else:
        queue.append([A, b, a + c - A])

    # c -> b
    if b + c < B:
        queue.append([a, b + c, 0])
    else:
        queue.append([a, B, b + c - B])

for index in range(201):
    if result[index]:
        print(index, end=" ")
