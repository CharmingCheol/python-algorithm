"""
1.이분 그래프 정의
 - 그래프 정점의 집합을 둘로 분할하고, 각 집합에 속한 정점끼리는 서로 인접하지 않을 때
   그러한 그래프를 이분 그래프라고 함
 - 여기서 중요한 점은 같은 그룹에 속한 정점끼리는 간선이 존재하면 안된다
2.이분 그래프 확인 방법
 - 간선이 생기는 경우는 다음과 같다
    > 자신의 node -> 다른 node로 가는 경우
    > 다른 node -> 자신의 node로 오는 경우
    > graph[x].append(y)  # 종착 node 넣어주기
      graph[y].append(x)  # 종착 node에서 자신으로 올 수도 있음
 - 현재 열에 방문하지 않았으면 DFS, BFS 로직을 처리
 - 다음 열을 아직 방문하지 않았으면, 방문 처리하고 DFS, BFS 로직을 처리
 - 다음 열에 이미 방문을 했는데 현재 열과 같은 색상이면 같은 그룹이기 때문에,
   이분 그래프가 아니게 됨
 - 위 모든 과정을 거쳤는데 이상이 없다면 이분 그래프가 됨
"""

import sys


def DFS(cur, graph, visited, color):
    for next in graph[cur]:
        if not visited[next]:  # 다음 열 방문여부 체크
            visited[next] = True  # 다음 열 방문 체크
            color[next] = False if color[cur] else True  # 다음 열에는 현재 열과 반대 색상을 칠함
            if DFS(next, graph, visited, color) is False:
                return False
        elif color[next] == color[cur]:  # 이미 방문한 곳이면서 자신과 색상이 같은 경우
            return False
    return True


repeat = int(sys.stdin.readline())
for _ in range(repeat):
    node, edge = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(node + 1)]  # 각 열에 0을 넣지 않고 빈 배열로 선언
    visited = [0] * (node + 1)  # 방문여부 체크
    color = [0] * (node + 1)  # 같은 그룹끼리 같은 색을 갖도록 해주는 배열
    flag = True
    for _ in range(edge):
        x, y = map(int, sys.stdin.readline().split())
        graph[x].append(y)  # 종착 node 넣어주기
        graph[y].append(x)  # 종착 node에서 자신으로 올 수도 있음
    for i in range(1, node + 1):
        if not visited[i]:  # 현재 열을 탐색하지 않았을 경우
            visited[i] = True  # 현재 열에 방문했음을 체크
            if DFS(i, graph, visited, color) is False:
                flag = False
                break
    print("YES" if flag else "NO")

