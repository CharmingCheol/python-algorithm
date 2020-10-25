""" 문제풀이
1.패턴 찾기
 - 스티커 하나를 선택하면 상하좌우에 있는 스티커는 선택할 수 없게 된다.
 - 그래서 1번째 열에서는 스티커를 각각 선택했다고 가정한다
 - 2번째 열에서는 왼쪽 대각선 위(왼쪽 대각선 아래)의 값과 자신의 값을 더해준다.
 - 3번째 열에서는 왼쪽 대각선 위(왼쪽 대각선 아래)의 값, 그 바로 왼쪽의 값 중에서
   최댓값을 선택해준다. 그리고 그 값과 자신의 값을 더해준다.
2.예시
 - 예시는 스크린샷에 있음
3.점화식
 - 열이 2일 경우
    > dp[0][1] = dp[1][0] + table[0][1]
    > dp[1][1] = dp[0][0] + table[1][1]
 - 열이 3이상일 경우
    > dp[0][index] = table[0][index] + max(dp[1][index - 2], dp[1][index - 1])
    > dp[1][index] = table[1][index] + max(dp[0][index - 2], dp[0][index - 1])
"""

import sys

for _ in range(int(sys.stdin.readline())):
    size = int(sys.stdin.readline())
    table = [list(map(int, sys.stdin.readline().split())) for _ in range(2)]
    dp = [[0] * size for _ in range(2)]
    dp[0][0] = table[0][0]
    dp[1][0] = table[1][0]
    for index in range(1, size):
        if index == 1:
            dp[0][1] = dp[1][0] + table[0][1]
            dp[1][1] = dp[0][0] + table[1][1]
        else:
            dp[0][index] = table[0][index] + max(dp[1][index - 2], dp[1][index - 1])
            dp[1][index] = table[1][index] + max(dp[0][index - 2], dp[0][index - 1])
    print(max(dp[0][size - 1], dp[1][size - 1]))