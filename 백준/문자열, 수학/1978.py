arr = [False, False] + [True] * 1000
for i in range(2, 1000):
    if arr[i]:
        for j in range(2 * i, 1000, i):
            arr[j] = False
repeat = list(map(int, input().split()))
count = 0
for r in repeat:
    if arr[r]:
        count += 1
print(count)

""" 방법2
Case = int(input())
num_list = list(map(int, input().split()))
result = 0
for i in num_list:
    cnt = 0
    if i == 1:
        continue
    for j in range(2, i + 1):
        if i % j == 0:
            cnt += 1
    if cnt == 1:
        result += 1
print(result)"""
