import sys


def DFS(y):
    global count
    for (x, num) in enumerate(board[y]):
        if check[x] == 0 and board[y][x] == 1:
            count += 1
            check[x] = 1
            DFS(x)


size = int(sys.stdin.readline())
virus = int(sys.stdin.readline())
board = [[0] * size for _ in range(size)]
check = [0] * size
check[0] = 1
count = 0

for _ in range(virus):
    (y, x) = map(int, sys.stdin.readline().split())
    board[y - 1][x - 1] = 1
    board[x - 1][y - 1] = 1
DFS(0)
print(count)
