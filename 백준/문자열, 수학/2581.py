arr = [False,False] + [True] * 100
for i in range(2, len(arr)):
    if arr[i]:
        for j in range(2 * i, len(arr), i):
            arr[j] = False
MIN = int(input())
MAX = int(input())
result = []
for num in range(MIN, MAX+1):
    if arr[num]:
        result.append(num)
print(sum(result))
print(min(result))
