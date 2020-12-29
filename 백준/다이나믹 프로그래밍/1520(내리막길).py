import sys


def DFS(y, x):
    if y == height and x == width:
        return 1
    if dp[y][x] == -1:
        dp[y][x] = 0
        for around_y, around_x in around:
            next_y = around_y + y
            next_x = around_x + x
            if 0 < next_y <= height and 0 < next_x <= width:
                if board[next_y - 1][next_x - 1] < board[y - 1][x - 1]:
                    dp[y][x] += DFS(next_y, next_x)
    return dp[y][x]


height, width = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(height)]
dp = [[-1] * (width + 1) for _ in range(height + 1)]
around = [[-1, 0], [0, 1], [1, 0], [0, -1]]
print(DFS(1, 1))
