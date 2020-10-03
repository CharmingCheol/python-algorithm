import sys

kind, money = map(int, sys.stdin.readline().split())
coins = list(filter(
    lambda x: x < money,
    [int(sys.stdin.readline()) for _ in range(kind)]
))
coins.sort(reverse=True)

result = 0
for coin in coins:
    if money // coin:
        result += money // coin
        money %= coin
print(result)
