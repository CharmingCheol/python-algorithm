import sys

sys.stdin = open("input.txt")

kind, money = map(int, sys.stdin.readline().split())
coins = [int(sys.stdin.readline()) for _ in range(kind)]
dp = [money + 1] * (money + 1)
dp[0] = 0

for y in range(kind):
    coin = coins[y]
    for x in range(coin, money + 1):
        dp[x] = min(dp[x], dp[x - coin] + 1)
print(-1 if dp[money] == money + 1 else dp[money])
