import sys

sys.stdin = open("input.txt")

size = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
dp = [0] * size
dp[0] = nums[0]

for y in range(1, size):
    temp = 0
    for x in range(y - 1, -1, -1):
        if nums[x] < nums[y] and temp < dp[x]:
            temp = dp[x]
    temp += nums[y]
    dp[y] = temp
print(max(dp))