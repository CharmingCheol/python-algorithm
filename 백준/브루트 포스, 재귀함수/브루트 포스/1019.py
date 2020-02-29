from sys import stdin

page = int(stdin.readline())
ans = [0] * 10
point, start = 1, 1


# 파라미터로 받은 x를 10으로 나누며 자리수를 나눠 ans배열에 더한다.
def cal(x, ans, point):
    while x > 0:
        ans[int(x % 10)] += point
        x = int(x / 10)


while start <= page:
    # page의 끝자리 9로 만들기
    while page % 10 != 9 and start <= page:
        cal(page, ans, point)
        page -= 1
    if page < start:
        break
    # start의 끝자리 0으로 만들기
    while start % 10 != 0 and start <= page:
        cal(start, ans, point)
        start += 1
    start /= 10
    page /= 10
    for i in range(10):
        ans[i] += int(page - start + 1) * point  # 반복되는 등장횟수를 더해준다.
    point *= 10  # 다음 자리수로 넘어가기 위해 * 10을 해준다
print(*ans)

"""
https://www.slideshare.net/Baekjoon/baekjoon-online-judge-1019
https://dundung.tistory.com/36
"""

""" 시간초과
num = int(stdin.readline())
arr = [0] * 10
for i in range(1, num + 1):
    while i >= 1:
        arr[int(i % 10)] += 1
        i /= 10
print(*arr)
"""