import sys

node, line = map(int, sys.stdin.readline().split())
graph = list([0] * node for _ in range(node))

for _ in range(line):
    y, x, cost = map(int, sys.stdin.readline().split())
    graph[y - 1][x - 1] = cost
for item in graph:
    print(item)