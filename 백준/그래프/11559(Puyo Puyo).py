import sys

sys.stdin = open("input.txt")


def DFS(y, x, color, path):
    visited[y][x] = False
    for around_y, around_x in around:
        next_y = around_y + y
        next_x = around_x + x
        if 0 <= next_y < 12 and 0 <= next_x < 6:
            if board[next_y][next_x] == color and visited[next_y][next_x]:
                path.append([next_y, next_x])
                DFS(next_y, next_x, color, path)
    return path


board = [list(map(str, sys.stdin.readline().strip())) for _ in range(12)]
around = [[-1, 0], [0, 1], [1, 0], [0, -1]]
result = 0
while True:
    puyo = []
    visited = [[True] * 6 for _ in range(12)]
    for y in range(11, - 1, -1):
        for x in range(6):
            if board[y][x] != "." and visited[y][x]:
                hit = DFS(y, x, board[y][x], [[y, x]])
                if 4 <= len(hit):
                    for hit_y, hit_x in hit: puyo.append([hit_y, hit_x])
    if not len(puyo): break
    for puyo_y, puyo_x in puyo:
        board[puyo_y][puyo_x] = "."
    for y in range(11, -1, -1):
        for x in range(6):
            if y < 11 and board[y][x] != ".":
                temp_y = y
                while temp_y != 11:
                    if board[temp_y + 1][x] != ".": break
                    swap = board[temp_y + 1][x]
                    board[temp_y + 1][x] = board[temp_y][x]
                    board[temp_y][x] = swap
                    temp_y += 1
    result += 1
print(result)
