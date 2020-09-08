import sys


def DFS(score, time, start, index):
    global result
    if time <= limit and result < score:
        result = score
    if index == limit - 1:
        return
    for i in range(start, size):
        item_score, item_time = map(int, nums[i])
        if time + item_time <= limit:
            DFS(score + item_score, time + item_time, i + 1, index + 1)
        else:
            DFS(score, time, i + 1, index + 1)


size, limit = map(int, sys.stdin.readline().split())
nums = []
result = 0
for _ in range(size):
    nums.append(list(map(int, sys.stdin.readline().split())))
DFS(0, 0, 0, 0)
print(result)
