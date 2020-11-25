import sys
from collections import deque


def DFS(depth):
    global result
    if depth == size:
        temp = 0
        for index in range(size - 1):
            temp += abs(stack[index] - stack[index + 1])
        result = max(result, temp)
        return
    for index in range(size):
        if check[index] == 0:
            check[index] = 1
            stack.append(nums[index])
            DFS(depth + 1)
            check[index] = 0
            stack.pop()


size = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
check = [0] * size
stack = deque()
result = 0
DFS(0)
print(result)
