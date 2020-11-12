import sys

sys.setrecursionlimit(10 ** 6)


def DFS(start, matrix, result):
    for e, d in matrix[start]:
        if result[e] == 0:
            result[e] = result[start] + d
            DFS(e, matrix, result)


V = int(sys.stdin.readline())
matrix = [[] for _ in range(V + 1)]
for _ in range(V):
    path = list(map(int, sys.stdin.readline().split()))
    for i in range(1, len(path) - 1, 2):
        matrix[path[0]].append([path[i], path[i + 1]])

# 첫번째 DFS결과
result1 = [0 for _ in range(V + 1)]
DFS(1, matrix, result1)  # 아무노드에서 시작해준다.
result1[1] = 0  # 임의의 기준점은 0으로 초기화

tmpmax = 0  # 최대값 구하기
index = 0  # 최장경로 노드
for i in range(V + 1):
    if tmpmax < result1[i]:
        tmpmax = result1[i]
        index = i

# 최장경로 노드에서 다시 DFS를 통해 트리지름구하기
result2 = [0 for _ in range(V + 1)]
DFS(index, matrix, result2)
result2[index] = 0  # 최장경로 지점은 초기화
print(max(result2))
