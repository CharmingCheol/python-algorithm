import sys

# 판자
size = int(sys.stdin.readline())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(size)]

# 기준점에서 8방향 상대좌표
around = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]

# queue
queue = []
count = 0

for y in range(size):
    for x in range(size):
        if board[y][x] == 1:
            board[y][x] = 0
            queue.append((y, x))  # 해당 좌표를 큐에 추가
            # BFS
            while queue:
                (now_y, now_x) = queue.pop(0)  # 현재 지점 popLeft
                # 현재 지점에서 8방향 탐색
                for (around_y, around_x) in around:
                    next_y = now_y + around_y
                    next_x = now_x + around_x
                    # 범위에 들어가고, 다음 장소가 1인 경우
                    if 0 <= next_y < size and 0 <= next_x < size and board[next_y][next_x] == 1:
                        board[next_y][next_x] = 0
                        queue.append((next_y, next_x))
            count += 1
print(count)
