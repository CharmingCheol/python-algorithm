import sys

height, width = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(height)]

dp = [[0] * (width + 1) for _ in range(height + 1)]
for y in range(1, height + 1):
    for x in range(1, width + 1):
        dp[y][x] = board[y - 1][x - 1] + max(dp[y - 1][x], dp[y][x - 1], dp[y - 1][x - 1])
print(dp[height][width])
