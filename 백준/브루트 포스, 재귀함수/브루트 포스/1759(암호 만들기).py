import sys
from collections import deque


def DFS(start, repeat):
    if repeat == limit:
        coll = 0  # 홀수
        cons = 0  # 짝수
        for item in stack:
            if item in "aeiou":
                coll += 1
            else:
                cons += 1
        if coll >= 1 and cons >= 2:
            for item in stack:
                print(item, end="")
            print()
        return
    for index in range(start, size):
        stack.append(alpha[index])
        DFS(index + 1, repeat + 1)
        stack.pop()


limit, size = map(int, sys.stdin.readline().split())
alpha = list(map(str, sys.stdin.readline().split()))
alpha.sort()
stack = deque()
DFS(0, 0)
