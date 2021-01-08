import sys
import heapq


def dijkstra(departure):
    # 현재 지점 0으로 초기화
    dp[departure] = 0

    # 현재 위치, 현재 가중치를 heap 배열에 추가
    heap = []
    heapq.heappush(heap, [departure, 0])

    while heap:
        now_position, now_weight = heapq.heappop(heap)
        # 최단 거리가 아닌 경우 continue
        if dp[now_position] < now_weight:
            continue
        # 인접 노드 탐색
        for next_position, next_weight in graph[now_position]:
            # 현재 가중치 + 다음 가중치
            total_weight = now_weight + next_weight
            # 현재 가중치가 더 크다면 교체
            if total_weight < dp[next_position]:
                dp[next_position] = total_weight
                # 다음 위치, weight 합계를 배열에다가 추가
                heapq.heappush(heap, [next_position, total_weight])


node = int(sys.stdin.readline())
path = int(sys.stdin.readline())
graph = [[] for _ in range(node + 1)]
dp = [float("inf") for _ in range(node + 1)]
for _ in range(path):
    start, end, cost = map(int, sys.stdin.readline().split())
    graph[start].append([end, cost])
departure, arrival = map(int, sys.stdin.readline().split())
dijkstra(departure)
print(dp[arrival])
