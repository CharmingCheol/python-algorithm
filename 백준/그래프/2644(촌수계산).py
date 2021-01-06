import sys


def DFS(y, depth):
    global result
    if y == end:
        if y < result:
            result = depth
        return
    for x in range(1, size + 1):
        if matrix[y][x] and visited[x][y]:
            visited[y][x] = 0
            DFS(x, depth + 1)


size = int(sys.stdin.readline())
start, end = map(int, sys.stdin.readline().split())
matrix = [[0] * (size + 1) for _ in range(size + 1)]
visited = [[1] * (size + 1) for _ in range(size + 1)]
result = 2164000000

for _ in range(int(sys.stdin.readline())):
    x, y = map(int, sys.stdin.readline().split())
    matrix[x][y] = matrix[y][x] = 1
DFS(start, 0)
print(-1 if result == 2164000000 else result)
