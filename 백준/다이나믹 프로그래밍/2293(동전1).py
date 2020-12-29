import sys

sys.stdin = open("input.txt")

kind, cost = map(int, sys.stdin.readline().split())
nums = [int(sys.stdin.readline()) for _ in range(kind)]

dp = [[0] * (cost + 1) for _ in range(2)]
for y in range(1, kind + 1):
    weight = nums[y - 1]
    for x in range(1, cost + 1):
        if x == weight:
            dp[1][x] = dp[1][x - weight] + dp[0][x] + 1
        elif x < weight:
            dp[1][x] = dp[0][x]
        else:
            dp[1][x] = dp[1][x - weight] + dp[0][x]
    dp[0] = dp[1]
print(dp[1][cost])
