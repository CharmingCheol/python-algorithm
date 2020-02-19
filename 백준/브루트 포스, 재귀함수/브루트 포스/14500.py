from sys import stdin

b = [
    [(0, 0), (0, 1), (1, 0), (1, 1)],
    [(0, 0), (0, 1), (0, 2), (0, 3)],
    [(0, 0), (1, 0), (2, 0), (3, 0)],
    [(0, 0), (0, 1), (0, 2), (1, 0)],
    [(1, 0), (1, 1), (1, 2), (0, 2)],
    [(0, 0), (1, 0), (1, 1), (1, 2)],
    [(0, 0), (0, 1), (0, 2), (1, 2)],
    [(0, 0), (1, 0), (2, 0), (2, 1)],
    [(2, 0), (2, 1), (1, 1), (0, 1)],
    [(0, 0), (0, 1), (1, 0), (2, 0)],
    [(0, 0), (1, 0), (1, 1), (2, 1)],
    [(0, 0), (0, 1), (1, 1), (2, 1)],
    [(0, 0), (0, 1), (0, 2), (1, 1)],
    [(0, 0), (1, 1), (1, 0), (0, 1)],
    [(0, 0), (1, 0), (2, 0), (1, 1)],
    [(1, 0), (2, 0), (0, 1), (1, 1)],
    [(0, 0), (1, 0), (1, 1), (2, 1)],
    [(1, 0), (0, 1), (1, 1), (0, 2)],
    [(0, 0), (1, 0), (1, 1), (2, 0)]
]


def tetromino(x, y):
    global result
    for i in range(19):
        criterion = 0
        for j in range(4):
            try:
                cx = x + b[i][j][0]
                cy = y + b[i][j][1]
                criterion += arr[cx][cy]
            except IndexError:
                continue
        result = max(result, criterion)


N, M = map(int, stdin.readline().split())
arr = [list(map(int, stdin.readline().split())) for _ in range(N)]
result = 0
for i in range(N):
    for j in range(M):
        tetromino(i, j)
print(result)

"""
https://rebas.kr/792
https://jeongchul.tistory.com/670
"""
