import sys

# 상하좌우 좌표
coord = [[-1, 0], [0, - 1], [0, 1], [1, 0]]

# 사과나무 격자판
size = int(sys.stdin.readline())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(size)]

# 다음 수확할 장소 좌표 저장
queue = list()
queue.append([size // 2, size // 2])

# 수확한 장소의 재방문 방지
check = [[0] * size for _ in range(size)]
check[size // 2][size // 2] = 1

# 합계
count = 0
result = board[size // 2][size // 2]

while True:
    if count == size // 2:
        break
    for _ in range(len(queue)):
        (now_y, now_x) = queue.pop(0)
        for (coord_y, coord_x) in coord:
            calc_y = coord_y + now_y
            calc_x = coord_x + now_x
            if 0 <= calc_y < size and 0 <= calc_x < size:
                if check[calc_y][calc_x] == 0:
                    result += board[calc_y][calc_x]
                    queue.append([calc_y, calc_x])
                    check[calc_y][calc_x] = 1
    count += 1
print(result)