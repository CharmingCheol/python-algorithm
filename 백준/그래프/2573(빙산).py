import sys
from collections import deque

height, width = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(height)]
around = [[-1, 0], [0, 1], [1, 0], [0, -1]]
result = 0

while True:
    zero_coord = []
    iceberg_count = 0
    iceberg_check = [[True] * width for _ in range(height)]
    for y in range(height):
        for x in range(width):
            for around_y, around_x in around:
                next_y = around_y + y
                next_x = around_x + x
                if 0 <= next_y < height and 0 <= next_x < width and board[y][x] == 0 and 0 < board[next_y][next_x]:
                    if board[next_y][next_x] - 1 == 0:
                        board[next_y][next_x] = -1
                        zero_coord.append([next_y, next_x])
                    else:
                        board[next_y][next_x] -= 1
    for y, x in zero_coord:
        board[y][x] = 0
    for y in range(height):
        for x in range(width):
            if board[y][x] != 0 and iceberg_check[y][x]:
                iceberg_count += 1
                iceberg_check[y][x] = False
                queue = deque([(y, x)])
                while queue:
                    now_y, now_x = queue.popleft()
                    for around_y, around_x in around:
                        next_y = around_y + now_y
                        next_x = around_x + now_x
                        if 0 <= next_y < height and 0 <= next_x < width:
                            if board[next_y][next_x] != 0 and iceberg_check[next_y][next_x]:
                                iceberg_check[next_y][next_x] = False
                                queue.append((next_y, next_x))
    if 2 <= iceberg_count:
        print(result + 1)
        break
    elif iceberg_count == 0:
        print(0)
        break
    result += 1
