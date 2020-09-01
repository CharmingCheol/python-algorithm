import sys

limit, pick = map(int, sys.stdin.readline().split())
temp = [0] * pick
count = 0


def DFS(index):
    global count
    if index == pick:
        for item in temp:
            print(item, end=" ")
        print()
        count += 1
        return
    for item in range(limit):
        temp[index] = item + 1
        DFS(index + 1)


DFS(0)
print(count)
