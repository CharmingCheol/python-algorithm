import sys


def DAC(y, x, size):
    if size == 1:
        board[y][x] = "*"
        return
    for i in range(3):
        for j in range(3):
            if i * 3 + j != 4:
                next_y = y + i * (size // 3)
                next_x = x + j * (size // 3)
                DAC(next_y, next_x, size // 3)


size = int(sys.stdin.readline())
board = [[" " for _ in range(size)] for _ in range(size)]
DAC(0, 0, size)
for y in range(size):
    for x in range(size):
        print(board[y][x], end="")
    print()
