# 동적 프로그래밍
n = int(input())  # 반복 횟수
t = []  # 상담 소요일
p = []  # 상담 금액
dp = []  # 최대 수령 금액
for i in range(n):
    a, b = map(int, input().split())
    t.append(a)
    p.append(b)
    dp.append(b)
dp.append(0)
for i in range(n - 1, -1, -1):  # 6부터 시작해서 0까지 역순으로 진행
    # 퇴사일을 벗어났을 때(ex. 8일차에 퇴사하는데 7일차 때 3일치에 있음)
    if t[i] + i > n:
        # dp[i + 1]값을 넣고 위에서 dp.append(0)을 넣었으니 예시와 같이
        # 7일차 때 3일치에 일이 있으니 dp[6]은 0이 됨
        dp[i] = dp[i + 1]
    # 퇴사일을 벗어나지 않을 경우
    else:
        # i가 4일 경우
        # dp[i + 1] = 0, p[i] + dp[i + t[i]] = 15 + 0
        # i가 3일 경우
        # dp[i + 1] = 15, p[i] + dp[i + t[i]] = 20 + 15
        dp[i] = max(dp[i + 1], p[i] + dp[i + t[i]])
print(dp[0])

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# 브루트 포스 방식
from sys import stdin


def money(day, total):
    global ans
    if day >= quitDay:
        # ans 값 갱신
        ans = max(ans, total)
        return
    if day + T[day] <= quitDay:
        # 일을 했을 경우
        money(day + T[day], total + P[day])
    # 다음날 이동
    money(day + 1, total)


quitDay = int(stdin.readline())
T, P = [], []
ans = 0
for i in range(quitDay):
    t, p = map(int, stdin.readline().split())
    T.append(t)
    P.append(p)
money(0, 0)
print(ans)

"""
https://pacific-ocean.tistory.com/199
https://www.fenslett.com/entry/%EB%B0%B1%EC%A4%80-14501-%ED%87%B4%EC%82%AC
"""
