""" 플이과정
1.점화식
 - dp[index] = dp[index - 3] + dp[index - 2] + dp[index - 1]
"""
import sys

case = int(sys.stdin.readline())
nums = [int(sys.stdin.readline()) for _ in range(case)]
dp = [0] * 11
dp[1] = 1
dp[2] = 2
dp[3] = 4

for index in range(4, 11):
    dp[index] = dp[index - 3] + dp[index - 2] + dp[index - 1]
for num in nums:
    print(dp[num])