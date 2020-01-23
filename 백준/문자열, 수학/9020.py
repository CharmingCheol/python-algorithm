check = [False, False] + [True] * 10001
for a in range(2, 10001):
    if check[a]:
        for b in range(2 * a, 10001, a):
            check[b] = False
for _ in range(int(input())):
    number = int(input())
    start = number // 2
    end = start
    for c in range(10001):
        if check[start] and check[end]:
            print(start, end)
            break
        start -= 1
        end += 1

""" 시간 초과 2
for _ in range(int(input())):
    boolArr = [False, False] + [True] * 10001
    arr = []
    for b in range(2, 10001):
        if boolArr[b]:
            for c in range(2 * b, 10001, b):
                boolArr[c] = False
            arr.append(b)
    number = int(input())
    print(boolArr)
    stop = True
    start = 0
    end = 0
    for d in arr:
        for e in arr:
            if number - d - e == 0:
                stop = False
                start = d
                end = e
                break
        if not stop: break
    print(start, end)
"""


""" 시간 초과 2
for i in range(int(input())):
    num = int(input())
    arr = []
    for a in range(num):
        cnt = 0
        if a == 1:
            continue
        for b in range(2, a + 1):
            if a % b == 0:
                cnt += 1
        if cnt == 1:
            arr.append(a)
    start = 0
    end = 0
    stop = True
    for c in arr:
        for d in arr:
            if num - c - d == 0:
                start = c
                end = d
                stop = False
                break
        if stop == False:
            break
    print(start, end)
"""