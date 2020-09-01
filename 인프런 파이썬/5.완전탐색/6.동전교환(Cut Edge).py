import sys

size = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
nums.sort(reverse=True)
count = int(sys.stdin.readline())

flag = True
result = 2164000000


def DFS(temp, index):
    global result, flag
    if not flag: return
    if temp > count: return
    if temp == count or index == size:
        result = index
        flag = False
        return
    for item in nums:
        DFS(temp + item, index + 1)


DFS(0, 0)
print(result)
