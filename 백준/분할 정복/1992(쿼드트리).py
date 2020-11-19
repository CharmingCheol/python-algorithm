import sys


def DAC(y, x, size):
    global string
    if size == 1:
        string += str(board[y][x])
        return board[y][x]
    target = board[y][x]
    for i in range(y, size + y):
        for j in range(x, size + x):
            if target != board[i][j]:
                string += "("
                for k in range(2):
                    for l in range(2):
                        next_y = y + k * (size // 2)
                        next_x = x + l * (size // 2)
                        DAC(next_y, next_x, size // 2)
                string += ")"
                return
    string += str(board[y][x])

size = int(sys.stdin.readline())
board = [list(map(int, sys.stdin.readline().strip())) for _ in range(size)]
string = ""
DAC(0, 0, size)
print(string)
