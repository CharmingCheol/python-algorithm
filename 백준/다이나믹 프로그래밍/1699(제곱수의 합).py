"""
1.패턴 찾기
 - 현재 수보다 작은 제곱의 수들을 전부 구해야 한다.
    > 현재 수 : 13, 제곱의 수들 : 1, 4, 9
 - 현재 수로 오는 방법은 제곱의 수를 더해야만 올 수 있기 때문이다.
    > 13으로 오는 방법은 12+1, 9+4, 4+9밖에 없음
 - 즉, 현재 수 - 제곱의 수를 뺀 값의 dp 인덱스 값들을 배열에다가 추가한다.
   그리고 거기서 가장 작은 값에다가 1을 더한 경우가 최소값이 된다
"""

import sys

num = int(sys.stdin.readline())
squared = [item * item for item in range(1, 317)]
dp = [0] * (num + 1)

for i in range(1, num + 1):
    temp = []
    for j in squared:
        if i < j:
            break
        temp.append(dp[i - j])
    dp[i] = min(temp) + 1
print(dp[num])
