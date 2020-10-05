import sys

money = int(sys.stdin.readline())
balance = 1000 - money
coins = [500, 100, 50, 10, 5, 1]
result = 0

for coin in coins:
    if balance // coin:
        result += balance // coin
        balance %= coin
print(result)