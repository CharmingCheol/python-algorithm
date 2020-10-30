import sys


def DFS(startNode):
    visited[startNode] = 1
    print(startNode, end=" ")
    for x in range(1, node + 1):
        if visited[x] == 0 and path[startNode][x] == 1:
            DFS(x)


def BFS(startNode):
    queue = [startNode]
    visited[startNode] = 1
    while queue:
        startNode = queue.pop(0)
        print(startNode, end=" ")
        for x in range(1, node + 1):
            if visited[x] == 0 and path[startNode][x] == 1:
                queue.append(x)
                visited[x] = 1


node, edge, startNode = map(int, sys.stdin.readline().split())
path = [[0] * (node + 1) for size in range(node + 1)]
visited = [0] * (node + 1)
for _ in range(edge):
    start, end = map(int, sys.stdin.readline().split())
    path[start][end] = 1
    path[end][start] = 1

DFS(startNode)
visited = [0] * (node + 1)
print()
BFS(startNode)