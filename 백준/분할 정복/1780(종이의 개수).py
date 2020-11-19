import sys


def DAC(y, x, size):
    if size == 1:
        index = board[y][x]
        count[index] += 1
        return
    target = board[y][x]
    for i in range(y, size + y):
        for j in range(x, size + x):
            if target != board[i][j]:
                for k in range(3):
                    for l in range(3):
                        next_y = y + k * (size // 3)
                        next_x = x + l * (size // 3)
                        DAC(next_y, next_x, size // 3)
                return
    index = board[y][x]
    count[index] += 1


size = int(sys.stdin.readline())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(size)]
count = {-1: 0, 0: 0, 1: 0}
DAC(0, 0, size)
for item in count.values():
    print(item)
