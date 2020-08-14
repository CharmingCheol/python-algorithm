import sys

board = [list(map(str, sys.stdin.readline().split())) for _ in range(7)]
count = 0
for first_index in range(len(board)):
    for second_index in range(3):
        horizontal = ""
        vertical = ""
        for third_index in range(second_index, second_index + 5):
            horizontal += board[first_index][third_index]
            vertical += board[third_index][first_index]
        if horizontal == horizontal[::-1]:
            count += 1
        if vertical == vertical[::-1]:
            count += 1
print(count)
