import sys
from collections import deque


def BFS(sheep, wolf, y, x):
    visited[y][x] = False
    queue = deque([(y, x)])
    sheep_count = sheep
    wolf_count = wolf
    while queue:
        now_y, now_x = queue.popleft()
        for around_y, around_x in around:
            next_y = around_y + now_y
            next_x = around_x + now_x
            if 0 <= next_y < height and 0 <= next_x < width:
                if visited[next_y][next_x] and board[next_y][next_x] != "#":
                    visited[next_y][next_x] = False
                    queue.append((next_y, next_x))
                    if board[next_y][next_x] == "o":
                        sheep_count += 1
                    elif board[next_y][next_x] == "v":
                        wolf_count += 1
    return [0, wolf_count] if sheep_count <= wolf_count else [sheep_count, 0]


height, width = map(int, sys.stdin.readline().split())
board = [list(map(str, sys.stdin.readline().strip())) for _ in range(height)]
visited = [[True] * width for _ in range(height)]
around = [[-1, 0], [0, 1], [1, 0], [0, -1]]
sheep_result = 0
wolf_result = 0
for y in range(height):
    for x in range(width):
        if visited[y][x]:
            if board[y][x] == "v":
                result = BFS(0, 1, y, x)
                sheep_result += result[0]
                wolf_result += result[1]
            elif board[y][x] == "o":
                result = BFS(1, 0, y, x)
                sheep_result += result[0]
                wolf_result += result[1]
print(sheep_result, wolf_result)
