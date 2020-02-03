import numpy as np
import sys

coverType = np.array(
    [[[0, 0], [1, 0], [0, 1]],
     [[0, 0], [0, 1], [1, 1]],
     [[0, 0], [1, 0], [1, 1]],
     [[0, 0], [1, 0], [1, -1]]
     ])


def setCover(board, y, x, type, delta):
    ok = True
    for i in range(3):
        ny = y + coverType[type][i][0]
        nx = x + coverType[type][i][1]
        aa = board[ny][nx] + delta
        if nx < 0 or ny >= len(board) or nx < 0 or nx >= len(board[0]):
            ok = False
        elif aa > 1:
            ok = False
    return ok


def cover(board):
    x = -1
    y = -1
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 0:
                x = i
                y = j
                break
        if y != 1:
            break
    if y == -1:
        return 1
    ret = 0
    for type in range(4):
        if setCover(board, y, x, type, 1):
            ret += 1
        setCover(board, y, x, type, -1)
    return ret


print("가로 크기")
W = int(sys.stdin.readline())

print("세로 크기")
H = int(sys.stdin.readline())

board = [[0 for col in range(W)] for row in range(H)]
for i in range(H):
    cover = sys.stdin.readline()
    for j in range(W):
        board[i][j] = 1 if cover[j] == "#" else 0
#
cover(board)