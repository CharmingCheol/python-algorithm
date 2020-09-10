import sys


def DFS(index, total):
    if index == size:
        if 0 < total <= total_height:
            result.add(total)
        return
    DFS(index + 1, total + nums[index])
    DFS(index + 1, total - nums[index])
    DFS(index + 1, total)


size = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
total_height = sum(nums)
result = set()
DFS(0, 0)
print(total_height - len(result))