import numpy as np

dx = np.array([-1, -1, -1, 1, 1, 1, 0, 0])
dy = np.array([-1, 1, 0, -1, 0, 1, -1, 1])


def has_word(y, x, word):
    # 기저 1: board의 범위를 벗어나는 경우
    if (y > len(board)) or (x > len(board[0])):
        return False
    # 기저 2: 첫 글자가 좌표의 위치의 글자와 다를 경우
    if board[y][x] != word[0]:
        return False
    # 기저 3: 글자가 1개면 더 이상 비교할 게 남아 있지 않음
    if len(word) == 1:
        return True
    for direction in range(8):
        next_y = y + dy[direction]
        next_x = x + dx[direction]
        # 여기까지 왔다는 것은 이미 첫 글자가 일치한 경우이므로
        # 그 다음 글자부터 다시 시작
        # 한 방향으로 무식하게 파고 들어가는 완전 탐색
        if has_word(next_y, next_x, word[1:]):
            return True
    return False


board = np.array([['U', 'R', 'L', 'P', 'M'],
                  ['X', 'P', 'R', 'E', 'T'],
                  ['G', 'I', 'A', 'E', 'T'],
                  ['X', 'T', 'N', 'Z', 'Y'],
                  ['X', 'O', 'Q', 'R', 'S']])

print(has_word(2, 0, 'GIRL'))
