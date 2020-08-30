import sys

size = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
total = sum(nums)
flag = False


def DFS(index, temp):
    global flag
    if flag: return
    if index >= size:
        return
    else:
        if temp == total - temp:
            flag = True
            return print("YES")
        else:
            next = index + 1
            DFS(next, temp + nums[next - 1])
            DFS(next, temp)


DFS(0, 0)
if not flag: print("NO")
