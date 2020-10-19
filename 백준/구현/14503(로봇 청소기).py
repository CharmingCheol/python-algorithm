import sys

sys.stdin = open("input.txt")

N, M = map(int, sys.stdin.readline().split())
r, c, d = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
rotate = [[-1, 0], [0, -1], [1, 0], [0, 1]]
warning = 0
count = 0

while True:
    # 4방향 모두 0이 없을 경우
    if warning == 4:
        (back_y, back_x) = rotate[d - 2]
        # 바라보는 기준으로 뒤가 벽일 경우
        if board[r + back_y][c + back_x] == 1:
            print(d)
            break
        # 뒤가 벽이 아닐 경우
        else:
            r += back_y
            c += back_x
            warning = 0
    # 현재 칸이 0인 경우
    if board[r][c] == 0:
        board[r][c] = 2
        warning = 0
        count += 1
    # 왼쪽으로 회전
    if d == 3:
        d = 0
    else:
        d += 1
    # 방향 회전 후 다음 칸으로 진행할 수 있는지 확인
    (rotate_y, rotate_x) = rotate[d]
    if board[r + rotate_y][c + rotate_x] == 1 or board[r + rotate_y][c + rotate_x] == 2:
        warning += 1
    else:
        r += rotate_y
        c += rotate_x
