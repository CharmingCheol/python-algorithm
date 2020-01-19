import sys

arr = []
for _ in range(int(sys.stdin.readline())):
    arr.append(list(map(int, sys.stdin.readline().strip().split())))
arr.sort(key=lambda x: (x[0], x[1]))
for i in arr:
    print(i[0], i[1])

""" lambda
비교할 아이템의 요소가 복수 개일 경우, 튜플로 그 순서를 내보내주면 된다.
ex. sorted(e, key = lambda x : (x[0], -x[1]))
-를 붙이면, 현재 정렬차순과 반대로 하게 된다.
"""