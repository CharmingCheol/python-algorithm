import sys


def DFS(index, a, b, c):
    global result
    if index == size:
        min_num = min(a, min(b, c))
        max_num = max(a, max(b, c))
        gap = max_num - min_num
        if gap < result:
            length = len({a, b, c})
            if length == 3:
                result = gap
        return
    DFS(index + 1, a + nums[index], b, c)
    DFS(index + 1, a, b + nums[index], c)
    DFS(index + 1, a, b, c + nums[index])


size = int(sys.stdin.readline())
nums = list()
result = 2164000000
for _ in range(size):
    nums.append(int(sys.stdin.readline()))
DFS(0, 0, 0, 0)
print(result)
