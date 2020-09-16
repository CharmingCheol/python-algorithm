import sys


def DFS(y, x):
    global count
    # 목적지에 도착한 경우
    if y == max_coord[0] and x == max_coord[1]:
        count += 1
        return
    now = board[y][x]
    for (around_y, around_x) in around:
        next_y = y + around_y
        next_x = x + around_x
        # 사각형 범위 안에 들어가있는지 체크
        if 0 <= next_y < size and 0 <= next_x < size:
            next = board[next_y][next_x]
            # 다음 방문지가 더 크고, 방문하지 않은 곳인지 체크
            if now < next and check[next_y][next_x] == 0:
                check[next_y][next_x] = 1  # 방문 체크
                DFS(next_y, next_x) # 재귀
                check[next_y][next_x] = 0  # 백트래킹


size = int(sys.stdin.readline())  # 정사각형 길이
board = []  # 정사각형 판
around = [[-1, 0], [0, 1], [1, 0], [0, -1]]  # 기준점에서 상하좌우 상대좌표
min_coord = [0, 0]  # 최소 높이 좌표
max_coord = [0, 0]  # 최대 높이 좌료
count = 0  # 목적지까지 갈 수 있는 경우의 수

for y in range(size):
    nums = list(map(int, sys.stdin.readline().split()))
    board.append(nums)
    for x in range(size):
        (min_y, min_x) = min_coord
        (max_y, max_x) = max_coord
        # 최솟값 좌표 갱신
        if board[min_y][min_x] > board[y][x]:
            min_coord = [y, x]
        # 최댓값 좌표 갱신
        if board[max_y][max_x] < board[y][x]:
            max_coord = [y, x]

# 방문지 체크하는 배열 생성
check = [[0] * size for _ in range(size)]
check[min_coord[0]][min_coord[1]] = 1

DFS(min_coord[0], min_coord[1])
print(count)
