## 정의
- 다이나믹 프로그래밍을 활용한 대표적인 최단 경로 탐색 알고리즘
- 특정한 하나의 정점에서 다른 모든 정점으로 가는 최단 경로를 알려줌

## 핵심
- 다익스트라가 다이나믹 프로그래밍인 이유는 최단거리는 여러개의 최단 거리로 이루어져 있기 때문. 즉, 작은 문제들이 큰 문제의 부분 집합으로 속해있다고 할 수 있음
- 하나의 최단 거리를 구할 때 그 이전까지 구했던 최단 거리 정보를 그대로 사용

## 동작 과정
##### 1.출발 노드를 설정
##### 2.출발 노드를 기준으로 각 노드의 최소 비용을 저장
##### 3.방문하지 않은 노드 중에서 가장 비용이 적은 노드를 선택
##### 4.해당 노드를 거쳐서 특정한 노드로 가는 경우를 고려하여 최소 비용을 갱신
##### 5.3번, 4번 과정을 반복

## 개선
- 선형탐색으로 다익스트라를 찾으면 시간 복잡도가 O^2가 됨
- 만약 정점의 갯수는 많지만 간선의 갯수가 현저히 적다면 선형탐색 방식은 비효율적
- 힙의 특징을 이용한다면 nlogn의 시간복잡도를 가질 수 있음

#### 첫번째 코드(O^2)
```python
# 가장 최소 거리를 가지는 정점을 반환
def getSmallIndex():
    minValue = INF
    index = 0
    for i in range(node):
        # 방문하지 않은 노드 중에서 현재 최소값보다 더 작은 노드가 존재한다면
        if distance[i] < minValue and not visited[i]:
            minValue = distance[i]
            index = i
    return index


def dijkstra(start):
    # 출발 노드를 기준으로 각 노드의 최소 비용을 저장
    for i in range(node):
        distance[i] = matrix[start][i]
    # 시작점은 방문처리
    visited[start] = True
    for i in range(node - 2):
        current = getSmallIndex()  # 최소 인덱스 가져오기
        visited[current] = True  # 방문 처리
        # 인접 노드 탐색
        for j in range(node):
            if not visited[j]:  # 현재 노드를 방문하지 않았다면
                # 현재 위치의 최소 비용 + 그 노드를 거쳐서 간 값 < 그 노드로 가는 최소 비용
                if distance[current] + matrix[current][j] < distance[j]:
                    distance[j] = distance[current] + matrix[current][j]  # 작은 값으로 갱신


INF = 1000000000  # 무한 값
node = 6  # 정점의 갯수
# 대각선 기준 대칭구조
matrix = [
    [0, 2, 5, 1, INF, INF],
    [2, 0, 3, 2, INF, INF],
    [5, 3, 0, 3, 1, 5],
    [1, 2, 3, 0, 1, INF],
    [INF, INF, 1, 1, 0, 2],
    [INF, INF, 5, INF, 2, 0]
]
visited = [0] * node  # 방문한 노드 체크
distance = [0] * node  # 노드 별 최단 거리

dijkstra(0)
print(distance)
```

#### 두번째 코드(nlogn)
```python
mycountry = {
    "A": {"B": 8, "C": 1, "D": 2},
    "B": {},
    "C": {"B": 5, "D": 2},
    "D": {"E": 3, "F": 5},
    "E": {"F": 1},
    "F": {"A": 5},
}


def dijkstra(road, start):
    # 최초에 inf로 초기화
    country = {node: float("inf") for node in road}
    # 시작점을 0으로 갱신
    country[start] = 0
    # 시작점 인덱스, 시작점을 heap 배열에 추가
    heap = []
    heapq.heappush(heap, [country[start], start])

    while heap:
        now_distance, now_position = heapq.heappop(heap)
        # 최단 거리가 아닌 경우 continue
        if country[now_position] < now_distance:
            continue
        # 현재 노드의 인접 노드를 탐색
        for arrival, weight in road[now_position].items():
            distance = now_distance + weight  # 선택된 노드를 거쳐서 인접 노드로 가는 비용
            # 기존 최소 비용보다 더 저렴하다면 교체
            if distance < country[arrival]:
                country[arrival] = distance
                heapq.heappush(heap, [now_distance, arrival])
    return country


INF = 1000000000  # 무한 값
node = 6  # 정점의 갯수
print(dijkstra(mycountry, "A"))
```