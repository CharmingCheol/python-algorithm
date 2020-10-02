import sys

kind, size = map(int, sys.stdin.readline().split())
nums = [list(map(int, sys.stdin.readline().split())) for _ in range(kind)]
dp = [0] * (size + 1)

for y in range(kind):
    (weight, value) = nums[y]
    for x in range(weight, size + 1):
        if dp[x] < dp[x - weight] + value:
            dp[x] = dp[x - weight] + value
print(dp[size])