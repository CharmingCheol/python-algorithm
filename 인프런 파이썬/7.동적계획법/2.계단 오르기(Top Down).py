import sys


def DFS(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if temp[n] != 0:
        return temp[n]
    temp[n] = DFS(n - 2) + DFS(n - 1)
    return temp[n]


num = int(sys.stdin.readline())
temp = [0] * (num + 1)
DFS(num)
print(temp[num])
