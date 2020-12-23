import sys

sys.stdin = open("input.txt")
size = int(sys.stdin.readline())
dp = []

for _ in range(size):
    dp.append(list(map(int, sys.stdin.readline().split())))

for i in range(1, size):
    for j in range(i + 1):
        if j == 0:
            dp[i][j] = dp[i][j] + dp[i - 1][0]
        elif j == i:
            dp[i][j] = dp[i][j] + dp[i - 1][i - 1]
        else:
            dp[i][j] = dp[i][j] + max(dp[i - 1][j - 1], dp[i - 1][j])
print(max(dp[size - 1]))