import sys
from collections import deque


def BFS():
    check = [-1] * (height + 1)
    check[depart] = 0
    queue = deque()
    queue.append(depart)
    while queue:
        now = queue.popleft()
        if now == dest: return check[dest]
        if now + up <= height and check[now + up] == -1:
            check[now + up] = check[now] + 1
            queue.append(now + up)
        if 0 < now - down and check[now - down] == -1:
            check[now - down] = check[now] + 1
            queue.append(now - down)
    return "use the stairs"


height, depart, dest, up, down = map(int, sys.stdin.readline().split())
print(BFS())
