import sys

tetrominos = [
    # ㅡ자
    [(0, 0), (1, 0), (2, 0), (3, 0)],
    [(0, 0), (0, 1), (0, 2), (0, 3)],
    # ㅁ자
    [(0, 0), (0, 1), (1, 0), (1, 1)],
    # ㄱ자
    [(0, 0), (0, 1), (0, 2), (1, 0)],
    [(0, 0), (0, 1), (0, 2), (1, 2)],
    [(0, 0), (1, 0), (2, 0), (2, 1)],
    [(0, 1), (1, 1), (2, 1), (2, 0)],
    [(0, 0), (1, 0), (2, 0), (0, 1)],
    [(0, 1), (1, 1), (2, 1), (0, 0)],
    [(0, 0), (1, 0), (1, 1), (1, 2)],
    [(1, 0), (1, 1), (1, 2), (0, 2)],
    # 번개
    [(0, 1), (1, 1), (1, 0), (2, 0)],
    [(0, 0), (1, 0), (1, 1), (2, 1)],
    [(0, 1), (0, 2), (1, 0), (1, 1)],
    [(0, 0), (0, 1), (1, 1), (1, 2)],
    # ㅗ자
    [(0, 0), (0, 1), (0, 2), (1, 1)],
    [(1, 0), (0, 1), (1, 1), (2, 1)],
    [(0, 1), (1, 0), (1, 1), (1, 2)],
    [(0, 0), (1, 0), (2, 1), (1, 1)],
]

height, width = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(height)]
result = 0
for y in range(height):
    for x in range(width):
        for tetromino in tetrominos:
            temp = 0
            count = 0
            for (tetromino_y, tetromino_x) in tetromino:
                if y + tetromino_y >= height or x + tetromino_x >= width:
                    break
                count += 1
                temp += board[y + tetromino_y][x + tetromino_x]
            if count == 4 and result < temp:
                result = temp
print(result)