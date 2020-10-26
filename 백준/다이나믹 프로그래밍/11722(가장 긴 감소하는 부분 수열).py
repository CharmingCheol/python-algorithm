"""
1.패턴 찾기
 - 10	30	10	20	20	10
   10	10	30	30	30	30
		    10	20	20	20
					    10
"""
import sys

size = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
dp = [1] * size

for y in range(1, size):
    temp = 0
    for x in range(y):
        if nums[y] < nums[x] and temp < dp[x]:
            temp = dp[x]
    dp[y] = temp + 1
print(dp[size - 1])
