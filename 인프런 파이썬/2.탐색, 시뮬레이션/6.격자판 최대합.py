import sys

size = int(sys.stdin.readline())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(size)]


# 대각선
def cross(size):
    result = -1
    total = 0
    # 좌측상단 -> 우측하단
    for index in range(size):
        result += board[index][index]
    # 우측상단 -> 좌측하단
    for index in range(size - 1, -1, -1):
        total += board[size - index - 1][index]
    return max(result, total)


# 가로 및 세로
def line(size):
    result = -1
    for first_index in range(size):
        vertical = 0
        horizontal = 0
        for second_index in range(size):
            vertical += board[second_index][first_index]
            horizontal += board[first_index][second_index]
        result = max(result, max(vertical, horizontal))
    return result


print(max(cross(size), line(size)))
