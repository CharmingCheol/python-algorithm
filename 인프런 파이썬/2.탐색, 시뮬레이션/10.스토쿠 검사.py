import sys

standard_coord = [[1, 1], [1, 4], [1, 7], [4, 1], [4, 4], [4, 7], [7, 1], [7, 4], [7, 7]]
around_coord = [[-1, -1], [0, -1], [1, -1], [-1, 0], [1, 0], [-1, 1], [0, 1], [1, 1]]

sudoku_board = [list(map(str, sys.stdin.readline().split())) for _ in range(9)]

check = True
# 가로 세로 체크
for first_index in range(len(sudoku_board)):
    vertical = ""
    horizontal = ""
    for second_index in range(len(sudoku_board)):
        vertical += sudoku_board[first_index][second_index]
        horizontal += sudoku_board[second_index][first_index]
    if len(vertical) != len(set(vertical)) or len(horizontal) != len(set(horizontal)):
        check = False
        break
if check:
    result = True
    # 3 * 3 크기 체크
    for (standard_x, standard_y) in standard_coord:
        small_board = str(sudoku_board[standard_x][standard_y])
        for (around_x, around_y) in around_coord:
            small_board += sudoku_board[standard_x - around_x][standard_y - around_y]
        if len(set(small_board)) != 9:
            result = False
            break
    print("YES" if result else "NO")
else:
    print("NO")
