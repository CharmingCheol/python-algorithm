import sys


def DFS(y):
    global count
    if y == node - 1:
        count += 1
        visited[node - 1] = 0
        print(path)
        return
    for x in range(node):
        if graph[y][x] == 1 and visited[x] == 0:
            visited[x] = 1
            path.append(x + 1)
            DFS(x)
            visited[x] = 0
            path.pop()


node, line = map(int, sys.stdin.readline().split())
graph = list([0] * node for _ in range(node))

visited = [0] * node
visited[0] = 1
path = list()
path.append(1)
count = 0

for _ in range(line):
    y, x = map(int, sys.stdin.readline().split())
    graph[y - 1][x - 1] = 1
DFS(0)
print(count)
