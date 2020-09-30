import sys

size = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))

dp = [0] * size
dp[0] = 1
result = 0

for start in range(1, size):
    for end in range(start - 1, -1, -1):
        if nums[end] < nums[start] and dp[start] < dp[end]:
            dp[start] = dp[end]
    dp[start] += 1
    if result < dp[start]:
        result = dp[start]
print(result)
