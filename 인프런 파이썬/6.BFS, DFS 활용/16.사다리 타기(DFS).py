import sys


def DFS(y, x):
    if y == 0:
        print(x)
        return
    check[y][x] = 1  # 현재 위치 체크
    # 왼쪽 탐색
    if 0 <= x - 1 and board[y][x - 1] == 1 and check[y][x - 1] == 0:
        DFS(y, x - 1)
    # 오른쪽 탐색
    elif x + 1 < 10 and board[y][x + 1] == 1 and check[y][x + 1] == 0:
        DFS(y, x + 1)
    # 위로 탐색
    elif board[y - 1][x] == 1 and check[y - 1][x] == 0:
        DFS(y - 1, x)


board = [list(map(int, sys.stdin.readline().split())) for _ in range(10)]
arrive = board[9].index(2)
check = [[0] * 10 for _ in range(10)]
DFS(9, arrive)
