from sys import stdin


def delivery(index, count):
    global result
    if index > len(chicken):
        return
    if count == M:
        totalDistance = 0
        for hx, hy in house:
            houseChicken = 1e9
            for j in distance:
                cx, cy = chicken[j]
                houseChicken = min(houseChicken, abs(hx - cx) + abs(hy - cy))
            totalDistance += houseChicken
        result = min(result, totalDistance)
        return
    distance.append(index)
    delivery(index + 1, count + 1)
    distance.pop()
    delivery(index + 1, count)


N, M = map(int, stdin.readline().split())
arr = [list(map(int, stdin.readline().split())) for _ in range(N)]
house, chicken, distance = [], [], []
result = 1e9
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            house.append((i + 1, j + 1))
        if arr[i][j] == 2:
            chicken.append((i + 1, j + 1))
delivery(0, 0)
print(result)

"""
https://rebas.kr/791
"""
