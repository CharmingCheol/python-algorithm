import sys

arr = []
for _ in range(int(sys.stdin.readline())):
    num = int(sys.stdin.readline().strip())
    arr.append(num)
arr.sort()
for result in arr:
    print(result)

""" 버블 정렬
arr = []
for _ in range(int(sys.stdin.readline())):
    num = int(sys.stdin.readline().strip())
    arr.append(num)
for index in range(len(arr) - 1):
    for index2 in range(len(arr) - index - 1):
        if arr[index2] > arr[index2 + 1]:
            arr[index2], arr[index2 + 1] = arr[index2 + 1], arr[index2]
print(arr) """

""" 삽입 정렬
arr = []
for _ in range(int(sys.stdin.readline())):
    num = int(sys.stdin.readline().strip())
    arr.append(num)
for index in range(1, len(arr)):
    while 0 < index and arr[index - 1] > arr[index]:
        arr[index - 1], arr[index] = arr[index], arr[index - 1]
        index -= 1
print(arr)"""