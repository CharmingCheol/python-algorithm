import numpy as np

dx = np.array([-1, -1, -1, 1, 1, 1, 0, 0])
dy = np.array([-1, 0, 1, -1, 0, 1, -1, 1])

board = np.array([['U', 'R', 'L', 'P', 'M'],
                  ['X', 'P', 'R', 'E', 'T'],
                  ['G', 'I', 'A', 'E', 'T'],
                  ['X', 'T', 'N', 'Z', 'Y'],
                  ['X', 'O', 'Q', 'R', 'S']])


def has_word(y, x, word):
    if (y > len(board)) or (x > len(board[0])):
        return False
    if board[y][x] != word[0]:
        return False
    if len(word) == 1:
        return True
    for i in range(len(dx)):
        standard_x = x + dx[i]
        standard_y = y + dy[i]
        if has_word(standard_y, standard_x, word[1:]):
            return True
    return False


print(has_word(2, 0, 'GIRL'))
