import sys


def DFS(y, x):
    global count
    for (around_y, around_x) in around:
        next_y = around_y + y
        next_x = around_x + x
        # 사각형 범위안에 들어가있는지 체크
        if 0 <= next_y < size and 0 <= next_x < size:
            # 다음 이동할 장소가 1인 경우
            if board[next_y][next_x] == 1:
                count += 1
                board[next_y][next_x] = 0  # 0으로 초기화
                DFS(next_y, next_x)  # 재귀


# 사각형 2차원 배열과 사각형 길이
size = int(sys.stdin.readline())
board = [list(map(int, sys.stdin.readline().strip())) for _ in range(size)]

# 기준점에서 상하좌우 상대좌표
around = [[-1, 0], [0, 1], [1, 0], [0, -1]]
count = 0  # 연결되어 있는 갯수 체크
result = []  # count를 담는 배열

for y in range(size):
    for x in range(size):
        # 해당 좌표가 1인 경우
        if board[y][x] == 1:
            DFS(y, x)  # DFS
            result.append(1 if count == 0 else count)
            count = 0  # 초기화

result.sort()
print(len(result))
for item in result:
    print(item)
