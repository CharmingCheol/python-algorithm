import sys
sys.setrecursionlimit(10 ** 6)


def DFS(y, x, index):
    for (around_y, around_x) in around:
        next_y = around_y + y
        next_x = around_x + x
        if 0 <= next_y < size and 0 <= next_x < size:
            if visited[next_y][next_x] == 1 and table[next_y][next_x] > index:
                visited[next_y][next_x] = 0
                DFS(next_y, next_x, index)


size = int(sys.stdin.readline())
table = [list(map(int, sys.stdin.readline().split())) for _ in range(size)]
around = [[-1, 0], [0, 1], [1, 0], [0, -1]]
result = 0

for index in range(101):
    count = 0
    visited = [[1] * size for _ in range(size)]
    for y in range(size):
        for x in range(size):
            if visited[y][x] == 1 and table[y][x] > index:
                count += 1
                visited[y][x] = 0
                DFS(y, x, index)
    result = max(result, count)
    if count == 0:
        break
print(result)
