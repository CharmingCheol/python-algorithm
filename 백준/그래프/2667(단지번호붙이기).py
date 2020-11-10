import sys

sys.setrecursionlimit(10 ** 6)


def DFS(y, x):
    global count
    for (around_y, around_x) in around:
        next_y = around_y + y
        next_x = around_x + x
        if 0 <= next_y < size and 0 <= next_x < size:
            if board[next_y][next_x] == "1":
                board[next_y][next_x] = "0"
                count += 1
                DFS(next_y, next_x)


size = int(sys.stdin.readline())
board = [list(map(str, sys.stdin.readline().strip())) for _ in range(size)]
check = []
around = [[-1, 0], [0, 1], [1, 0], [0, -1]]
count = 0
for y in range(size):
    for x in range(size):
        if board[y][x] == "1":
            count += 1
            board[y][x] = "0"
            DFS(y, x)
            check.append(count)
            count = 0
check.sort()
print(len(check))
for item in check:
    print(item)
