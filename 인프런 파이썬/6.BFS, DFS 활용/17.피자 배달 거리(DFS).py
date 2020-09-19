import sys


def DFS(index, start):
    global result
    if index == height:
        total = 0
        # 집 좌표
        for (house_y, house_x) in house:
            distance = 2147000000
            # 순열에 저장된 인덱스 위치에 따른 피자집 좌표 출력
            for temp in check:
                (pizza_y, pizza_x) = pizza[temp - 1]
                distance = min(distance, abs(pizza_y - house_y) + abs(pizza_x - house_x))
            total += distance
        if total < result:
            result = total
        return
    # 피자집 좌표를 순열로 저장
    for num in range(start, len(pizza)):
        check[index] = num + 1
        DFS(index + 1, num + 1)


width, height = map(int, sys.stdin.readline().split())
board = []  # 지도
house = []  # 집 좌표 저장
pizza = []  # 피자집 좌표 저장
check = [0] * height  # 피자집 좌표들을 height 크기만큼 순열로 저장
result = 2147000000

for y in range(width):
    line = list(map(int, sys.stdin.readline().split()))
    board.append(line)
    for (x, item) in enumerate(line):
        # 집인 경우
        if item == 1:
            house.append([y, x])
        # 피자집인 경우
        if item == 2:
            pizza.append([y, x])

DFS(0, 0)
print(result)
