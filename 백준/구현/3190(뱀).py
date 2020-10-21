import sys

size = int(sys.stdin.readline())
apple_count = int(sys.stdin.readline())
apple_coord = [list(map(int, sys.stdin.readline().split())) for _ in range(apple_count)]
direction_count = int(sys.stdin.readline())
direction = [list(map(str, sys.stdin.readline().split())) for _ in range(direction_count)]
direction_index = {"index": 0, "sec": int(direction[0][0])}

head = [0, 0]
change_direction = [0, 1]
trace = [[0, 0]]
timer = 0

board = [[0] * size for _ in range(size)]
board[0][0] = "S"
for (apple_y, apple_x) in apple_coord:
    board[apple_y - 1][apple_x - 1] = "A"

while True:
    timer += 1
    (head_y, head_x) = head
    (change_y, change_x) = change_direction
    next_y = head_y + change_y
    next_x = head_x + change_x
    # 벽에 부딪힐 경우
    if next_y < 0 or size <= next_y or next_x < 0 or size <= next_x:
        break
    # 자기 자신과 부딪힐 경우
    if board[next_y][next_x] == "S":
        break
    # 매 초 마다 뱀 이동
    if board[next_y][next_x] == "A":
        board[next_y][next_x] = 0
    else:
        (tail_y, tail_x) = trace.pop(0)
        board[tail_y][tail_x] = 0
    board[next_y][next_x] = "S"
    head = [next_y, next_x]
    trace.append([next_y, next_x])
    # 방향 전환해야 하는 초가 되었을 경우
    if timer == direction_index["sec"]:
        (index, sec) = direction_index.values()
        CD = direction[index][1]
        (y, x) = change_direction
        if index != direction_count - 1:
            direction_index = {"index": index + 1, "sec": int(direction[index + 1][0])}
        if y == 0 and x == 1:
            change_direction = [-1, 0] if CD == "L" else [1, 0]
        elif y == 1 and x == 0:
            change_direction = [0, 1] if CD == "L" else [0, -1]
        elif y == 0 and x == -1:
            change_direction = [1, 0] if CD == "L" else [-1, 0]
        elif y == -1 and x == 0:
            change_direction = [0, -1] if CD == "L" else [0, 1]
print(timer)