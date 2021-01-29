import sys
from collections import deque
input = sys.stdin.readline


def bfs(mid):
    visit[start] = 1  # 시작점 방문
    queue = deque()
    queue.append(start)
    while queue:
        now = queue.popleft()
        if now == end:
            return True
        for nx, nc in board[now]:  # 다음 이동지, 제한 무게
            if visit[nx] == 0 and mid <= nc:  # 아직 방문하지 않았고, 중간값이 제한 무게보다 낮거나 같다면
                queue.append(nx)
                visit[nx] = 1
    return False


island, repeat = map(int, input().split())
board = [[] for i in range(island + 1)]

for i in range(repeat):
    a, b, limit = map(int, input().split())
    board[a].append([b, limit])  # 양방향
    board[b].append([a, limit])  # 양방향
start, end = map(int, input().split())
left, right = 1, 1000000000

while left <= right:
    visit = [0 for i in range(island + 1)]
    mid = (left + right) // 2
    if bfs(mid):
        left = mid + 1
    else:
        right = mid - 1
print(right)
