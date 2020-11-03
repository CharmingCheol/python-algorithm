import sys

for _ in range(int(sys.stdin.readline())):
    num = int(sys.stdin.readline())
    dp = [0] * (num + 1)
    if num == 1 or num == 2 or num == 3:
        print(1)
        continue
    elif num == 4 or num == 5:
        print(2)
        continue
    for index in range(1, 6):
        if index == 1 or index == 2 or index == 3:
            dp[index] = 1
        elif index == 4 or index == 5:
            dp[index] = 2
    for index in range(6, num + 1):
        dp[index] = dp[index - 1] + dp[index - 5]
    print(dp[num])
