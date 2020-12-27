import sys

sys.stdin = open("input.txt")

size = int(sys.stdin.readline())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(size)]
dp = [[0] * size for _ in range(size)]
dp[0][0] = 1

for y in range(size):
    for x in range(size):
        if dp[y][x] and board[y][x]:
            now = board[y][x]
            move_y = now + y
            move_x = now + x
            if move_y < size:
                dp[move_y][x] += dp[y][x]  # 종착점에서 다 쓸어담음
            if move_x < size:
                dp[y][move_x] += dp[y][x]  # 종착점에서 다 쓸어담음
print(dp[-1][-1])
