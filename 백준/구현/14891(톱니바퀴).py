import sys


# 톱니바퀴 회전
def rotate(index, direction):
    # 시계 방향
    if direction == 1:
        pop = gear[index].pop()
        gear[index].insert(0, pop)
    # 반시계 방향
    elif direction == -1:
        pop = gear[index].pop(0)
        gear[index].append(pop)


# 왼쪽으로 회전
def turnLeftGear(index, teeth, direction):
    if index <= 0: return
    if gear[index][2] != teeth:
        sixth_teeth = gear[gear_index][6]
        rotate(index, direction)
        turnLeftGear(index - 1, sixth_teeth, -direction)


# 오른쪽으로 회전
def turnRightGear(index, teeth, direction):
    if 4 < index: return
    if gear[index][6] != teeth:
        second_teeth = gear[gear_index][2]
        rotate(index, direction)
        turnRightGear(index + 1, second_teeth, -direction)


gear = [list(map(int, sys.stdin.readline().strip())) for _ in range(4)]
gear.insert(0, [0])
turn_limit = int(sys.stdin.readline())
turn_info = [list(map(int, sys.stdin.readline().split())) for _ in range(turn_limit)]
result = 0

for (gear_index, direction) in turn_info:
    second_teeth = gear[gear_index][2]
    sixth_teeth = gear[gear_index][6]
    rotate(gear_index, direction)
    turnLeftGear(gear_index - 1, sixth_teeth, -direction)  # 왼쪽 바퀴들 회전
    turnRightGear(gear_index + 1, second_teeth, -direction)  # 오른쪽 바퀴들 회전

for index in range(1, 5):
    if gear[index][0] == 1:
        result += 2 ** (index - 1)
print(result)