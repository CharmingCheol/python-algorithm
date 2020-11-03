import sys

nums = list(map(int, sys.stdin.readline()))
size = len(nums)
nums = [0] + nums
dp = [1] * (size + 1)
if nums[1] == 0:
    print(0)
else:
    print(nums, dp)
    for index in range(2, size + 1):
        dp[index] = dp[index - 1]
        tensDigits = nums[index - 1] * 10 + nums[index]
        if 10 <= tensDigits <= 26:
            dp[index] += dp[index - 2]
    print(dp, dp[size] % 1000000)