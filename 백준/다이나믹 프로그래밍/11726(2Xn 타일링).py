""" 플이과정
1.문제 풀이
 - 먼저 육안으로도 직사각형의 갯수를 구할 수 있을 때 까지 그려봤다.
 - 2인 경우에는 2가 나왔고, 3인 경우에는 3이 나왔다. 그리고 4인 경우에는 5가 나왔다.
 - 여기까지 보면 이전에 나온 블록을 활용해서, 1×2, 2×1 타일을 적절히 배치시키면 된다
2.점화식
 - dp[n] = dp[n-2] + dp[n-1]
3.10007을 나눈 이유
 - 제출 결과 틀렸다는 내용을 확인했다.
 - 이유는 수가 점점 커질수록 각 value별로 int가 기하급수적으로 커지기 때문.
   이를 해결하기 위해 10007을 나머지로 나눴을 때 나머지 값으로 저장
 - https://www.acmicpc.net/board/view/52805
"""
import sys

num = int(sys.stdin.readline())
dp = [1] * (num + 1)
for index in range(2, num + 1):
    dp[index] = (dp[index - 2] + dp[index - 1]) % 10007
print(dp[num])
