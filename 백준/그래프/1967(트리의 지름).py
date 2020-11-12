import sys

sys.setrecursionlimit(10 ** 6)
sys.stdin = open("input.txt")


def DFS(start, matrix, result, visited):
    for e, d in matrix[start]:
        if result[e] == 0 and visited[e] == 0:
            visited[start] = 1
            result[e] = result[start] + d
            DFS(e, matrix, result, visited)


size = int(sys.stdin.readline())
matrix = [[] for _ in range(size + 1)]
visited = [0] * (size + 1)
for _ in range(size - 1):
    (index, node, dist) = map(int, sys.stdin.readline().split())
    matrix[index].append([node, dist])
    matrix[node].append([index, dist])
first = [0] * (size + 1)
DFS(1, matrix, first, visited)
first[1] = 0

tmpmax = 0  # 최대값 구하기
index = 0  # 최장경로 노드
for i in range(size + 1):
    if tmpmax < first[i]:
        tmpmax = first[i]
        index = i

second = [0] * (size + 1)
visited = [0] * (size + 1)
DFS(index, matrix, second, visited)
second[index] = 0  # 최장경로 지점은 초기화
print(max(second))
