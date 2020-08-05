import sys

# 풀이 1
result = -2164000000
for _ in range(int(sys.stdin.readline())):
    dice_result = list(map(int, sys.stdin.readline().split()))
    frequency = [0] * 6
    stash = 0
    for index in range(1, 7):
        frequency[index - 1] = dice_result.count(index)
    if 3 in frequency:
        stash = 10000 + (frequency.index(3) + 1) * 1000
    elif 2 in frequency:
        stash = 1000 + (frequency.index(2) + 1) * 100
    else:
        stash = max(dice_result) * 100
    if result < stash:
        result = stash
print(result)

# 풀이 2
result = -216400000
for _ in range(int(sys.stdin.readline())):
    dice = list(map(int, sys.stdin.readline().split()))
    money = 0
    if dice[0] == dice[1] and dice[1] == dice[2]:
        money = 10000 + dice[0] * 1000
    elif dice[0] == dice[1] or dice[0] == dice[2]:
        money = 1000 + dice[0] * 100
    elif dice[1] == dice[2]:
        money = 1000 + dice[1] * 100
    else:
        money = max(dice) * 100
    if result < money:
        result = money
print(result)