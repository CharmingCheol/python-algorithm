import sys

sys.setrecursionlimit(10 ** 6)
sys.stdin = open("input.txt")


def DFS(y):
    for x in range(1, node + 1):
        if check[x] == 0 and path[y][x] == 1:
            check[x] = 1
            DFS(x)


node, edge = map(int, sys.stdin.readline().split())
path = [[0] * (node + 1) for _ in range(node + 1)]
check = [0] * (node + 1)
result = 0

for _ in range(edge):
    start, end = map(int, sys.stdin.readline().split())
    path[start][end] = path[end][start] = 1
for y in range(1, node + 1):
    if check[y] == 0:
        DFS(y)
        result += 1
print(result)
