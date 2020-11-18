import sys

A, B = map(int, sys.stdin.readline().split())
n = list(map(int, sys.stdin.readline().split()))
m = list(map(int, sys.stdin.readline().split()))
nums = n + m
nums.sort()
print(" ".join(map(str, nums)))

""""""""""""""""""""""""""""""""""""""


def merge(temp, start, middle, end):
    i = start
    j = middle + 1
    k = start
    # 작은 순서대로 배열에 삽입
    while i <= middle and j <= end:
        if temp[i] <= temp[j]:
            array[k] = temp[i]
            i += 1
        else:
            array[k] = temp[j]
            j += 1
        k += 1
    # 남은 데이터도 추가적으로 삽입
    if i > middle:
        for index in range(j, end + 1):
            array[k] = temp[index]
            k += 1
    else:
        for index in range(i, middle + 1):
            array[k] = temp[index]
            k += 1
    # 정렬된 배열을 실제 배열에 삽입
    for index in range(start, end + 1):
        temp[index] = array[index]


def mergeSort(temp, start, end):
    # 크기가 1보다 큰 경우
    if start < end:
        middle = (start + end) // 2
        mergeSort(temp, start, middle)
        mergeSort(temp, middle + 1, end)
        merge(temp, start, middle, end)


A, B = map(int, sys.stdin.readline().split())
n = list(map(int, sys.stdin.readline().split()))
m = list(map(int, sys.stdin.readline().split()))
nums = n + m
size = A + B
array = [0] * size
mergeSort(nums, 0, size - 1)
print(nums)
