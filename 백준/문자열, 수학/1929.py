MIN, MAX = map(int, input().split())
arr = [False, False] + [True] * MAX
for i in range(2, len(arr)):
    if arr[i]:
        for j in range(2 * i, len(arr), i):
           arr[j] = False
for num in range(MIN, MAX+1):
    if arr[num]:
        print(num)

""" 방안1
Min, Max = list(map(int, input().split()))
arr = [False, False] + [True] * (Max - 1)
result = []
for i in range(2, Max + 1):
    if arr[i]:
        result.append(i)
    for j in range(2 * i, Max + 1, i):
        arr[j] = False
if Min == 1: Min = 2
for a in result[result.index(Min):len(result)]:
    print(a)
"""

""" 방안2
def result(num, Max):
    if num == 1:
        return False
    for a in range(2, Max + 1):
        if num / a == 1:
            return True
        if num % a == 0:
            return False
Min, Max = list(map(int, input().split()))
for i in range(Min, Max+1):
    if result(i, Max) == True:
        print(i)
"""
