import sys


# 사이클 문제
def DFS(start, current):
    # 현재 위치가 1인 경우
    if visited[current]:
        # 시작값과 현재값이 같은 경우(사이클인 경우)
        if start == current:
            result.append(start)
    else:
        visited[current] = 1
        DFS(start, nums[current])


size = int(sys.stdin.readline())
nums = [0] + [int(sys.stdin.readline()) for _ in range(size)]
visited = [0] * (size + 1)
result = []
for i in range(1, size + 1):
    DFS(i, i)
    visited = [0] * (size + 1)

print(len(result))
for item in result:
    print(item)
