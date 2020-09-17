import sys

sys.setrecursionlimit(10 ** 4)


def DFS(index, y, x):
    global check
    check[y][x] = 1
    for (around_y, around_x) in around:
        next_y = around_y + y
        next_x = around_x + x
        if 0 <= next_y < size and 0 <= next_x < size:
            if board[next_y][next_x] > index and check[next_y][next_x] == 0:
                DFS(index, next_y, next_x)


# 기준점 상하좌우 상대좌표
around = [[-1, 0], [0, 1], [1, 0], [0, -1]]

# 판자
size = int(sys.stdin.readline())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(size)]

result = 0
for index in range(99):
    check = [[0] * size for _ in range(size)]
    count = 0
    for y in range(size):
        for x in range(size):
            if check[y][x] == 0 and board[y][x] > index:
                count += 1
                DFS(index, y, x)
    if count == 0:
        break
    result = max(result, count)
print(result)
