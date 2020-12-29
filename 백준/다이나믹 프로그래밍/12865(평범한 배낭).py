import sys

"""
현재 무게가 기준 무게보다 적은 경우
바로 위에 있는 무게로 갱신
dp[y][x] = dp[y - 1][x]

현재 무게가 기준 무게보다 같거나 클 경우
max(바로 위 무게, 바로 위 무게에서 현재 무게를 빼고 현재 가치를 더한 값)
dp[y][x] = max(dp[y - 1][x], dp[y - 1][x - weight] + value)
"""

sys.stdin = open("input.txt")

kind, limit = map(int, sys.stdin.readline().split())
info = [list(map(int, sys.stdin.readline().split())) for _ in range(kind)]
dp = [[0] * (limit + 1) for _ in range(kind + 1)]

for y in range(1, kind + 1):
    weight, value = info[y - 1]
    for x in range(1, limit + 1):
        if x < weight:
            dp[y][x] = dp[y - 1][x]
        else:
            dp[y][x] = max(dp[y - 1][x], dp[y - 1][x - weight] + value)
print(dp[kind][limit])
