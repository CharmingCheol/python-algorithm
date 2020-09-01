import sys

limit, size = map(int, sys.stdin.readline().split())
nums = []
for _ in range(size):
    nums.append(int(sys.stdin.readline()))
result = 0
total = sum(nums)


def DFS(weight, index, check):
    global result, total
    if weight + (total - check) < result:
        return
    if weight > limit:
        return
    if index == size:
        result = weight if result < weight else result
        return
    else:
        result = weight if result < weight else result
        DFS(weight + nums[index], index + 1, check + nums[index])
        DFS(weight, index + 1, check + nums[index])


DFS(0, 0, 0)
print(result)
