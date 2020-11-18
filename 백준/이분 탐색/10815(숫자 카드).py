import sys

N = int(sys.stdin.readline())
cards = list(map(int, sys.stdin.readline().split()))
cards.sort()
M = int(sys.stdin.readline())
isCard = list(map(int, sys.stdin.readline().split()))

for item in isCard:
    left = 0
    right = N - 1
    flag = False
    while left <= right:
        mid = (left + right) // 2
        if cards[mid] == item:
            flag = True
            break
        if cards[mid] < item:
            left = mid + 1
        else:
            right = mid - 1
    print(1 if flag else 0, end=" ")
