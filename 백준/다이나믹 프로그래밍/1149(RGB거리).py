import sys

size = int(sys.stdin.readline())
dp = []

for _ in range(size):
    dp.append(list(map(int, sys.stdin.readline().split())))
for i in range(1, size):
    dp[i][0] = dp[i][0] + min(dp[i - 1][1], dp[i - 1][2])
    dp[i][1] = dp[i][1] + min(dp[i - 1][0], dp[i - 1][2])
    dp[i][2] = dp[i][2] + min(dp[i - 1][0], dp[i - 1][1])
print(min(dp[size - 1]))