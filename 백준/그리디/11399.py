import sys

size = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
nums.sort()

dp = [0] * size
dp[0] = nums[0]

for index in range(1, size):
    dp[index] = dp[index - 1] + nums[index]

print(sum(dp))