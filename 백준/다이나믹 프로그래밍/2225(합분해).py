import sys

sys.stdin = open("input.txt")

size, kind = map(int, sys.stdin.readline().split())
dp = [[0] * kind for _ in range(size)]

for i in range(kind):
    dp[0][i] = i + 1
for i in range(size):
    dp[i][0] = 1
for y in range(1, size):
    for x in range(1, kind):
        dp[y][x] = (dp[y][x - 1] + dp[y - 1][x]) % 1000000000
print(dp[size - 1][kind - 1])
