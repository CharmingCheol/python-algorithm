""" 플이과정
1.패턴 찾기
 - 먼저 길이가 n인 경우에 대해 이진수들을 다 구해봤다
    > n = 1 => 1
    > n = 2 => 10
    > n = 3 => 100 101
    > n = 4 => 1000 1001 1010
    > n = 5 => 10000 10001 10010 10100 1010
    > n = 6 => 100000 100001 100100 100101 101000 101001 101010

2.점화식 도출하기
 - 위 경우로 점화식을 도출하면, index -2, index - 1에 해당하는 값들을 더하면 된다.

3.점화식
 - 길이가 1, 2인 경우
    > 바로 1을 출력
 - 그 외(길이가 3이상인 경우)
    > dp[index] = dp[index - 2] + dp[index - 1]
"""
import sys

sys.stdin = open("input.txt")

num = int(sys.stdin.readline())
if num == 1 or num == 2:
    print(1)
else:
    dp = [0] * (num + 1)
    dp[1] = 1
    dp[2] = 1
    for index in range(3, num + 1):
        dp[index] = dp[index - 2] + dp[index - 1]
    print(dp[num])