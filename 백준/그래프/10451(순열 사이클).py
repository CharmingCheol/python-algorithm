import sys


def DFS(nums, array, index):
    if nums[index] != 0:
        nums[index] = 0
        DFS(nums, array, array[index] - 1)


for _ in range(int(sys.stdin.readline())):
    size = int(sys.stdin.readline())
    nums = list(index + 1 for index in range(size))
    array = list(map(int, sys.stdin.readline().split()))
    count = 0
    for index in range(size):
        if nums[index] != 0:
            nums[index] = 0
            DFS(nums, array, array[index] - 1)
            count += 1
    print(count)
