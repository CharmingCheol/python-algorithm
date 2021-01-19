import sys
from collections import deque

sys.stdin = open("input.txt")


def BFS():
    queue = deque([(0, 0, 0)])
    # 3차원 배열. 0번째 인덱스는 벽을 뚫지 않은 경우, 1번째 인덱스는 벽을 뚫은 경우
    visited = [[[-1] * 2 for _ in range(width)] for _ in range(height)]
    visited[0][0][0] = 1  # 최초 상태
    while queue:
        now_y, now_x, crushed = queue.popleft()
        for around_y, around_x in around:
            next_y = around_y + now_y
            next_x = around_x + now_x
            if 0 <= next_y < height and 0 <= next_x < width:
                # 다음 지점이 0이면서 아직 방문하지 않은 경우
                if board[next_y][next_x] == 0 and visited[next_y][next_x][crushed] == -1:
                    visited[next_y][next_x][crushed] = visited[now_y][now_x][crushed] + 1
                    queue.append((next_y, next_x, crushed))
                # 벽을 부순 횟수가 0회고, 다음 지점이 벽이면서 아직 방문하지 않은 경우
                elif crushed == 0 and board[next_y][next_x] == 1 and visited[next_y][next_x][1] == -1:
                    visited[next_y][next_x][1] = visited[now_y][now_x][0] + 1
                    queue.append((next_y, next_x, 1))
    return visited[height - 1][width - 1]


height, width = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().strip())) for _ in range(height)]
around = [[-1, 0], [0, 1], [1, 0], [0, -1]]

result1, result2 = BFS()
if result1 == -1 and result2 != 1:
    print(result2)
elif result1 != -1 and result2 == -1:
    print(result1)
else:
    print(min(result1, result2))
