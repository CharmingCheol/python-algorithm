import sys


def DFS(L, P):
    global count
    if L == size:
        count += 1
        for j in range(P):
            print(chr(temp[j] + 64), end='')
        print()
        return
    for i in range(1, 27):
        if nums[L] == i:
            temp[P] = i
            DFS(L + 1, P + 1)
        elif i >= 10 and nums[L] == i // 10 and nums[L + 1] == i % 10:
            temp[P] = i
            DFS(L + 2, P + 1)


nums = list(map(int, sys.stdin.readline()))
size = len(nums)
nums.insert(size, -1)
temp = [0] * size
count = 0
DFS(0, 0)
print(count)
