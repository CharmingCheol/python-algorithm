import sys
from collections import deque


def BFS():
    shark_y, shark_x = shark_coord
    queue = deque([(shark_y, shark_x, 0)])
    visited = [[True] * size for _ in range(size)]
    visited[shark_y][shark_x] = False
    result = []
    while queue:
        now_y, now_x, value = queue.popleft()
        for around_y, around_x in around:
            next_y = around_y + now_y
            next_x = around_x + now_x
            if 0 <= next_y < size and 0 <= next_x < size and visited[next_y][next_x]:
                # 물고기를 먹을 수 있는 경우
                if board[next_y][next_x] != 0 and board[next_y][next_x] < shark_size:
                    result.append([next_y, next_x, value + 1])  # 먹은 물고기의 좌표와 이동거리 값을 result에 추가
                    visited[next_y][next_x] = False
                # 아직 물고기는 못 먹지만, 다른 곳으로 이동이 가능한 경우
                elif board[next_y][next_x] <= shark_size:
                    queue.append((next_y, next_x, value + 1))
                    visited[next_y][next_x] = False
    return result


size = int(sys.stdin.readline())
board = []
around = [[-1, 0], [0, 1], [1, 0], [0, -1]]
shark_size = 2  # 상어 크기
shark_count = 0  # 상어가 물고기를 먹은 횟수
shark_coord = []  # 현재 상어 좌표
total_distance = 0  # 총 이동 거리

for y in range(size):
    line = list(map(int, sys.stdin.readline().split()))
    board.append(line)
    for x in range(size):
        if line[x] == 9:
            shark_coord = [y, x]

while True:
    result = BFS()
    if not len(result):
        print(total_distance)
        break
    final_coord = [1000, 1000]  # default 값은 1000
    distance = 1000  # default 값은 1000
    shark_y, shark_x = shark_coord
    for coord_y, coord_x, value in result:
        # 이동 거리가 더 짧은 경우
        if value < distance:
            distance = value
            final_coord = [coord_y, coord_x]
        # 이동 거리가 같은 경우
        elif value == distance:
            # 임시 지점보다 y 좌표가 더 가까운 곳에 있는 경우
            if coord_y < final_coord[0]:
                final_coord = [coord_y, coord_x]
            # y 좌표가 같으면서, 임시 지점보다 x 좌표가 더 가까운 경우
            elif final_coord[0] == coord_y and coord_x < final_coord[1]:
                final_coord = [coord_y, coord_x]
    # swap
    board[final_coord[0]][final_coord[1]] = 9
    board[shark_coord[0]][shark_coord[1]] = 0
    shark_coord = final_coord  # 상어 위치 갱신
    total_distance += distance  # 총 거리 갱신
    shark_count += 1  # 먹은 횟수 +1
    # 상어 크기와 먹은 횟수가 같은 경우
    if shark_count == shark_size:
        shark_size += 1
        shark_count = 0
