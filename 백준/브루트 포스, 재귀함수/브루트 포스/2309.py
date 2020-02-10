import sys

arr = []
for i in range(9):
    arr.append(int(sys.stdin.readline()))
arr.sort()
for i in range(len(arr)):
    result = sum(arr)
    flag = False
    for j in range(i, len(arr)):
        compare = arr[i] + arr[j]
        if result - compare == 100:
            flag = True
            arr.pop(i)
            arr.pop(j-1)
            break
    if flag:
        break
for i in arr:
    print(i)
