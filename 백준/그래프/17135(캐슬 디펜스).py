import sys
from itertools import combinations as cb
from copy import deepcopy


# 궁수의 사거리에 포함하는 곳을 (가중치, y, x) 배열로 저장
def get_distance(candidate):
    result = []
    for position_y, position_x in candidate:
        temp = []
        for y in range(height):
            for x in range(width):
                if abs(position_y - y) + abs(position_x - x) <= dist:
                    temp.append((abs(position_y - y) + abs(position_x - x), y, x))
        result.append(temp)
    return result


# 가장 가까운 위치에 있는 적 찾기
def find_nearest_enemy(area):
    area.sort(key=lambda x: (x[0], x[2]))
    for dist, y, x in area:
        if (y, x) in enemy_position:  # 활을 쏜 범위에 적이 있을 경우
            return (y, x)
    return None  # 다 돌았는데 적이 없으면 None


# 적을 아래로 한 칸씩 내리기
def go_forward():
    return set([(y + 1, x) for y, x in enemy_position if y + 1 < height])


height, width, dist = map(int, sys.stdin.readline().split())
archer_position = [(height, i) for i in range(width)]
candidates = cb(archer_position, 3)
enemy_position = set()
result = 0

# 적군의 좌표 저장
for y in range(height):
    line = list(map(int, sys.stdin.readline().split()))
    for x in range(width):
        if line[x] == 1:
            enemy_position.add((y, x))

for candidate in candidates:
    shoot_area = get_distance(candidate)  # 사수 별 사정 범위
    count = 0
    copy_enemy_position = deepcopy(enemy_position)
    while enemy_position:
        temp = set()
        for area in shoot_area:
            kill = find_nearest_enemy(area)  # 가장 가까운 위치에 있는 적 찾기
            if kill is not None:
                temp.add(kill)
        count += len(temp)
        enemy_position -= temp  # 죽은 적의 위치 없애기
        enemy_position = go_forward()  # 적군의 위치를 아래로 한칸씩 내리기
    enemy_position = copy_enemy_position  # 조작 된 적군 위치를 기존의 깊은 복사 한 배열로 갱신
    if result < count:
        result = count
print(result)
