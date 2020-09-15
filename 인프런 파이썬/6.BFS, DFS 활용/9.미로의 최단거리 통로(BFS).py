import sys

# 7 x 7 미로
board = [list(map(int, sys.stdin.readline().split())) for _ in range(7)]
coord = [[-1, 0], [0, - 1], [0, 1], [1, 0]]

# 이미 방문한 곳인지 체크
check = [0] * 49
check[0] = 1

# 다음 장소로 갈 수 있는 좌표 저장
queue = list()
queue.append([0, 0])

# 현재 방문한 곳과 출발 지점까지 간 거리 계산
distance = [0] * 49
flag = False

while len(queue) != 0:
    now = queue.pop(0)
    for (y, x) in coord:
        (now_y, now_x) = now
        calc_y = y + now_y
        calc_x = x + now_x
        # 7,7 좌표 찾음
        if calc_y == 6 and calc_x == 6:
            queue.clear()
            flag = True
            print(distance[(now_y * 7 + now_x)] + 1)
            break
        # board 좌표가 0이고, 이미 방문한 곳이 아닐 경우
        if 0 <= calc_x < 7 and 0 <= calc_y < 7:
            if board[calc_y][calc_x] == 0 and check[calc_y * 7 + calc_x] == 0:
                queue.append([calc_y, calc_x])
                check[calc_y * 7 + calc_x] = 1
                distance[calc_y * 7 + calc_x] = distance[(now_y * 7 + now_x)] + 1
if not flag:
    print(-1)
