import sys

size = int(sys.stdin.readline())
cards = list(map(int, sys.stdin.readline().split()))
dp = [0] * (size + 1)

for i in range(1, size + 1):
    card = cards[i - 1]
    for j in range(i, size + 1):
        dp[j] = max(dp[j], dp[j - i] + card)
print(dp[size])