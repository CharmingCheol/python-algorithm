import sys

size, target = map(int, sys.stdin.readline().split())
num_list = list(map(int, sys.stdin.readline().split()))
num_list.sort()

left = 0
right = size - 1
while left <= right:
    mid = (left + right) // 2
    if num_list[mid] == target:
        print(mid + 1)
        break
    elif num_list[mid] > target:
        right = mid - 1
    else:
        left = mid + 1
