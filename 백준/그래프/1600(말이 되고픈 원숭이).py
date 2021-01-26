import sys
from collections import deque

def BFS():
    # 3차원 배열
    visited = [[[-1] * (limit + 1) for _ in range(width)] for _ in range(height)]  # 각 원소의 길이를 limit의 값 만큼 확보
    visited[0][0][0] = 0  # 시작점 초기화
    queue = deque()
    queue.append([0, 0, 0])  # [y, x, count]
    while queue:
        now_y, now_x, count = queue.popleft()
        # 종료 지점 도달
        if now_y == height - 1 and now_x == width - 1:
            return visited[now_y][now_x][count]
        # 상하좌우 탐색
        for around_y, around_x in around:
            next_y = around_y + now_y
            next_x = around_x + now_x
            if 0 <= next_y < height and 0 <= next_x < width:
                if board[next_y][next_x] == 0 and visited[next_y][next_x][count] == -1:
                    visited[next_y][next_x][count] = visited[now_y][now_x][count] + 1
                    queue.append([next_y, next_x, count])
        # 나이트 점프 제한 횟수보다 작다면, 나이트 점프 가능
        if count < limit:
            for knight_y, knight_x in knight:
                next_y = knight_y + now_y
                next_x = knight_x + now_x
                if 0 <= next_y < height and 0 <= next_x < width:
                    if board[next_y][next_x] == 0 and visited[next_y][next_x][count + 1] == -1:
                        # 나이트 점프를 했으니 count를 1 증가
                        visited[next_y][next_x][count + 1] = visited[now_y][now_x][count] + 1
                        queue.append([next_y, next_x, count + 1])
    return -1


around = [[-1, 0], [0, 1], [1, 0], [0, -1]]  # 상하좌우 주변
knight = [[-1, 2], [-1, -2], [1, 2], [1, -2], [2, -1], [2, 1], [-2, -1], [-2, 1]]  # 나이트
limit = int(sys.stdin.readline())
width, height = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(height)]
print(BFS())