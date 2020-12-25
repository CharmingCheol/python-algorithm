import sys

sys.stdin = open("input.txt")

size = int(sys.stdin.readline())
dp = [1] * (size + 1)
dp[1] = 3
for i in range(2, size + 1):
    dp[i] = (dp[i - 1] * 2 + dp[i - 2]) % 9901
print(dp[size])
