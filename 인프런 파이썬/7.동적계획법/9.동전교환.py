import sys

size = int(sys.stdin.readline())
coins = list(map(int, sys.stdin.readline().split()))
money = int(sys.stdin.readline())

dp = [money] * (money + 1)
dp[0] = 0
for y in range(size):
    coin = coins[y]
    for x in range(coin, money + 1):
        if dp[x - coin] + 1 < dp[x]:
            dp[x] = dp[x - coin] + 1
print(dp[money])
