""" 플이과정
1.패턴 찾기
 - 이 문제의 패턴은 백준 10844(계단 수 찾기)와 비슷하다
    > https://www.acmicpc.net/problem/10844
 - 길이별로 가장 끝에 숫자들이 각각 몇번 나왔는지 표로 만들면 된다

2.점화식 도출하기
 - 길이가 1, 2인 경우의 표를 정리했다
    > 0  1  2  3  4  5  6  7  8  9
      1  1  1  1  1  1  1  1  1  1
      1  2  3  4  5  6  7  8  9  10
 - 같은 줄 좌측에 있는 수와 바로 위에 수를 더해주면 된다.

3.점화식
 - 끝자리가 0인 경우
    > dp[y][0] = 1
 - 그 외
    > dp[y][x] = dp[y][x - 1] + dp[y - 1][x]
"""
import sys

sys.stdin = open("input.txt")

num = int(sys.stdin.readline())
dp = [[0] * 10 for _ in range(num)]
dp[0] = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

for y in range(1, num):
    for x in range(10):
        if x == 0:
            dp[y][0] = 1
        else:
            dp[y][x] = dp[y][x - 1] + dp[y - 1][x]

print(sum(dp[num - 1]) % 10007)
