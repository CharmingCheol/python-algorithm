import sys


def DFS(time, pay):
    global result
    if time >= size and result < pay:
        result = pay
        return
    for i in range(time, size):
        item_time, item_pay = map(int, nums[i])
        if i + item_time <= size:
            DFS(i + item_time, pay + item_pay)
        DFS(i + 1, pay)


size = int(sys.stdin.readline())
nums = []
result = 0
for _ in range(size):
    nums.append(list(map(int, sys.stdin.readline().split())))
DFS(0, 0)
print(result)
