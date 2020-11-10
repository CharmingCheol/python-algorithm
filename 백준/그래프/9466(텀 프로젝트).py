import sys

sys.setrecursionlimit(10 ** 6)


def DFS(path, now, next):
    dfs_next = nums[next - 1]
    visited[now] = 1
    if now == next:
        done[now] = 1
        return
    elif visited[dfs_next] == 1 and now != next:
        visited[next] = 1
        done[next] = 1
        splice_index = path.index(dfs_next)
        for item in path[splice_index:]:
            done[item] = 1
        return
    if visited[dfs_next] == 0:
        visited[next] = 1
        path.append(next)
        DFS(path, next, dfs_next)


for _ in range(int(sys.stdin.readline())):
    size = int(sys.stdin.readline())
    nums = list(map(int, sys.stdin.readline().split()))
    visited = [0] * (size + 1)
    done = [0] * (size + 1)
    for (now, next) in enumerate(nums):
        if visited[next] == 0:
            DFS([now + 1], now + 1, next)
        else:
            visited[now + 1] = 1
    print(done.count(0) - 1)
