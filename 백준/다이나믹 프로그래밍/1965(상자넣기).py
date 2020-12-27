import sys

sys.stdin = open("input.txt")

size = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
dp = [0] * size
dp[0] = 1

for i in range(1, size):
    temp = 0
    for j in range(i - 1, -1, -1):
        if nums[j] < nums[i] and temp < dp[j]:
            temp = dp[j]
    dp[i] = temp + 1
print(max(dp))