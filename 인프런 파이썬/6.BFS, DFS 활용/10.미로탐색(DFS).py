import sys


def DFS():
    global count
    (now_y, now_x) = queue.pop(0)
    for (coord_y, coord_x) in coord:
        calc_y = now_y + coord_y
        calc_x = now_x + coord_x
        # 목적지에 도착한 경우
        if calc_x == 6 and calc_y == 6:
            count += 1
            return
        # 미로판 좌표 내에 있는지 체크
        if 0 <= calc_y < 7 and 0 <= calc_x < 7:
            # 해당 좌표가 갈 수 있는 곳이고, 방문한 적이 없는 곳인지 체크
            if maze[calc_y][calc_x] == 0 and check[calc_y * 7 + calc_x] == 0:
                check[calc_y * 7 + calc_x] = 1
                queue.append([calc_y, calc_x])
                DFS()
                check[calc_y * 7 + calc_x] = 0  # 벡트래킹


# 상하좌우 좌표
coord = [[-1, 0], [0, - 1], [0, 1], [1, 0]]

# 7 x 7 미로
maze = [list(map(int, sys.stdin.readline().split())) for _ in range(7)]

# 이미 방문한 곳인지 체크
check = [0] * 49
check[0] = 1

# 다음 장소로 갈 수 있는 좌표 저장
queue = list()
queue.append([0, 0])

# 도착 지점까지 갈 수 있는 경우 계산
count = 0
DFS()
print(count)
