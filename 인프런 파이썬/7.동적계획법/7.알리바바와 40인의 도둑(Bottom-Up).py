import sys

size = int(sys.stdin.readline())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(size)]

dp = [[0] * size for _ in range(size)]
dp[0][0] = board[0][0]
for index in range(1, size):
    dp[0][index] = dp[0][index - 1] + board[0][index]
    dp[index][0] = dp[index - 1][0] + board[index][0]

for y in range(1, size):
    for x in range(1, size):
        dp[y][x] = board[y][x] + min(dp[y - 1][x], dp[y][x - 1])
print(dp[size - 1][size - 1])