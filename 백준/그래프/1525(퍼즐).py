import sys
from collections import deque


def BFS(start):
    queue = deque([start])
    dist = dict()
    dist[start] = 0
    around = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    while queue:
        line = queue.popleft()
        if line == "123456780":
            return dist[line]
        zero = line.find("0")
        zero_y, zero_x = zero // 3, zero % 3
        for around_y, around_x in around:
            next_y = around_y + zero_y
            next_x = around_x + zero_x
            if 0 <= next_y < 3 and 0 <= next_x < 3:
                copyLine = list(line)
                nextIndex = next_y * 3 + next_x
                copyLine[nextIndex], copyLine[zero] = copyLine[zero], copyLine[nextIndex]
                join = "".join(copyLine)
                if not dist.get(join):
                    queue.append(join)
                    dist[join] = dist[line] + 1
    return - 1


start = ""
for _ in range(3):
    line = list(map(str, sys.stdin.readline().split()))
    for item in line:
        start += item
print(BFS(start))
