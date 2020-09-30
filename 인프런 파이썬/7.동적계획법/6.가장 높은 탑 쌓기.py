import sys

size = int(sys.stdin.readline())
nums = [list(map(int, sys.stdin.readline().split())) for _ in range(size)]
nums.sort(reverse=True)

dp = [0] * size
dp[0] = nums[0][1]
result = 0

for y in range(1, size):
    (square, height, weight) = nums[y]
    for x in range(y - 1, -1, -1):
        (x_square, x_height, x_weight) = nums[x]
        if weight < x_weight and dp[y] < dp[x]:
            dp[y] = dp[x]
    dp[y] += height
    result = max(result, dp[y])
print(result)
