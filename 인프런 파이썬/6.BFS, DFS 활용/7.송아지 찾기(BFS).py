import sys

MAX = 10000
flag = True
start, arrive = map(int, sys.stdin.readline().split())
# 한번 방문한 장소 체크
check = [0] * (MAX + 1)
check[start] = 1
# BFS 레벨 저장
count = [0] * (MAX + 1)
count[start] = 0
# BFS를 진행하기 위해 배열에다가 값을 저장
queue = []
queue.append(start)

while flag:
    now = queue.pop(0)
    next = [now - 1, now + 1, now + 5]
    if now == arrive:
        flag = False
        break
    for item in next:
        if 0 < item <= MAX and check[item] == 0:
            queue.append(item)
            check[item] = 1
            count[item] = count[now] + 1
print(count[arrive])
