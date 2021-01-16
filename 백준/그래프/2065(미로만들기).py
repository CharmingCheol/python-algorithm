import sys
from collections import deque


def BFS():
    queue = deque([(0, 0)])
    check[0][0] = 0
    while queue:
        now_y, now_x = queue.popleft()
        for around_y, around_x in around:
            next_y = now_y + around_y
            next_x = now_x + around_x
            if 0 <= next_y < size and 0 <= next_x < size and check[next_y][next_x] == -1:
                # 검은 방은 우선순위가 낮기 때문에, append로 넣어줌
                if board[next_y][next_x] == 0:
                    check[next_y][next_x] = check[now_y][now_x] + 1
                    queue.append((next_y, next_x))
                # 흰방에 높은 우선순위를 주기 위해 appendLeft를 해서 먼저 처리
                else:
                    check[next_y][next_x] = check[now_y][now_x]
                    queue.appendleft((next_y, next_x))

size = int(sys.stdin.readline())
board = [list(map(int, sys.stdin.readline().strip())) for _ in range(size)]
check = [[-1] * size for _ in range(size)]
around = [[-1, 0], [0, 1], [1, 0], [0, -1]]
BFS()
print(check[size - 1][size - 1])
