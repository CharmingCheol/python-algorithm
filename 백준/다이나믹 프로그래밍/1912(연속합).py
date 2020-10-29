"""
1.패턴 찾기
 - 이전 dp와 더하기 : dp[index - 1] + nums[index]
 - 이전 값과 더하기 : nums[index - 1] + nums[index]
 - 현재 입력값만 갖기 : nums[index]
2.점화식
 - dp[index] = max(case1, case2, case3)
"""
import sys

sys.stdin = open("input.txt")

size = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
dp = [0] * size
dp[0] = nums[0]

for index in range(1, size):
    case1 = dp[index - 1] + nums[index]
    case2 = nums[index]
    case3 = nums[index - 1] + nums[index]
    dp[index] = max(case1, case2, case3)
print(max(dp))
