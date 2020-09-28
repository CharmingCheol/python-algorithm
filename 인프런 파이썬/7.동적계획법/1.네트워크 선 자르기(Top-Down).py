import sys


def DFS(x):
    if x == 1: return 1
    if x == 2: return 2
    if temp[x] != 0: return temp[x]
    temp[x] = DFS(x - 2) + DFS(x - 1)
    return temp[x]


size = int(sys.stdin.readline())
temp = [0] * (size + 1)
DFS(size)
print(temp[size])
