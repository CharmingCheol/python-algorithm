import sys


def DFS(end, repeat, place):
    global result
    if repeat == pick:
        for item in temp:
            print(item, end=" ")
        print()
        result += 1
        return
    for index in range(end, size + 1):
        temp[place] = index
        DFS(index + 1, repeat + 1, place + 1)


size, pick = map(int, sys.stdin.readline().split())
temp = [0] * pick
result = 0
DFS(1, 0, 0)
print(result)
