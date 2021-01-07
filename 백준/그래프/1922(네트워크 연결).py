import sys


# 특정 노드의 부모 노드 찾기
def getParent(x):
    if graph[x] == x: return x  # 현재 노드가 부모의 노드가 같다면(자신을 가리킨다면)
    graph[x] = getParent(graph[x])  # 재귀로 자신의 부모 찾기
    return graph[x]


# 각 부모 노드를 합침. 더 작은 값으로 갱신
def unionParent(a, b):
    a = getParent(a)  # 부모 찾기
    b = getParent(b)  # 부모 찾기
    if a < b:
        graph[b] = a
    else:
        graph[a] = b


# 두 개의 노드가 같은 부모 노드를 가지는지 확인
def find(a, b):
    a = getParent(a)
    b = getParent(b)
    return True if a == b else False


node = int(sys.stdin.readline())
path = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(path)]
graph = [i for i in range(node + 1)]
total = 0

arr.sort(key=lambda value: value[2])
for i in range(len(arr)):
    a, b, distance = arr[i]
    # 동일한 부모값을 갖지 않는지(사이클이 형성하지 않는지)
    if not find(a, b):
        total += distance
        unionParent(a, b)  # 두 노드를 동일한 부모 노드 값으로 설정
print(total)