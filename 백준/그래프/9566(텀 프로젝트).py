import sys


def DFS(i):
    global result
    visited[i] = True
    cycle.append(i)
    num = numbers[i]
    # 다음 방문지가 체크되어 있는 경우
    if visited[num]:
        if num in cycle: # 현재 지점이 사이클에 포함되어 있을 경우
            result += cycle[cycle.index(num):] # 이전 경로는 제외
    # 아직 방문하지 않은 경우
    else:
        DFS(num)


for _ in range(int(input())):
    size = int(sys.stdin.readline())
    numbers = [0] + list(map(int, input().split()))
    visited = [True] + [False] * size
    result = []

    for index in range(1, size + 1):
        if not visited[index]:
            cycle = []
            DFS(index)
    print(size - len(result))
