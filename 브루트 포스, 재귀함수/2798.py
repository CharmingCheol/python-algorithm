import sys

card, Max = map(int, sys.stdin.readline().split())
cardList = list(map(int, sys.stdin.readline().split()))
result = 0
for a in range(len(cardList) - 2):
    for b in range(a + 1, len(cardList) - 1):
        for c in range(b + 1, len(cardList)):
            sumValue = cardList[a] + cardList[b] + cardList[c]
            if result < sumValue <= Max:
                result = sumValue
print(result)