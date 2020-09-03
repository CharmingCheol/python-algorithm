import sys


def DFS(total, repeat, end):
    global result
    if end == limit and total % multiple == 0:
        result += 1
        return
    for index in range(repeat, size):
        DFS(total + nums[index], index + 1, end + 1)


size, limit = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))
multiple = int(sys.stdin.readline())
result = 0

DFS(0, 0, 0)
print(result)