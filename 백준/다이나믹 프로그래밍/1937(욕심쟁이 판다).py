import sys

sys.setrecursionlimit(10 ** 6)


def DFS(y, x):
    global result
    if dp[y][x] == 0:
        dp[y][x] = 1
        for around_y, around_x in around:
            next_y = around_y + y
            next_x = around_x + x
            if 0 <= next_y < size and 0 <= next_x < size:
                if board[y][x] < board[next_y][next_x]:
                    dp[y][x] = max(dp[y][x], DFS(next_y, next_x) + 1)
        result = max(result, dp[y][x])
    return dp[y][x]


size = int(sys.stdin.readline())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(size)]
dp = [[0] * size for _ in range(size)]
around = [[-1, 0], [0, 1], [1, 0], [0, -1]]
result = 0

for y in range(size):
    for x in range(size):
        if dp[y][x] == 0:
            DFS(y, x)
print(result)