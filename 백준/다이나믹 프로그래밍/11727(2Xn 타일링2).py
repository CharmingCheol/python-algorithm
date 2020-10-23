""" 플이과정
1.문제 풀이
 - 가로가 1, 2인 경우에는 육안으로도 몇개인지 알 수 있다.
   1인 경우에는 1가지, 2인 경우에는 3가지이다.
 - 인덱스가 3인 경우부터 DP를 구해야 되는데, 현재 기준으로 -2인 곳에 곱하기 2를 하고,
   현재 기준 -1인 값과 더해서 값을 적용한다.
2.점화식
 - dp[index] = dp[index - 2] * 2 + dp[index - 1]
3.결과
 0  1  2  3  4   5   6   7   8    9    10
 0  1  3  5  11  21  43  85  171  341  683
"""
import sys

num = int(sys.stdin.readline())
dp = [0] * (num + 2)
dp[1] = 1
dp[2] = 3

for index in range(3, num + 1):
    dp[index] = (dp[index - 2] * 2 + dp[index - 1]) % 10007
print(dp[num], dp)
