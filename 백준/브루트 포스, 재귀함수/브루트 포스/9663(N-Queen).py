import sys


def DFS(index):
    global count
    if index == size:  # 모든 퀸을 다 배치한 경우
        count += 1
        return
    for i in range(size):
        # 모든 경우에서 0인 경우
        if row[i] + left[index + i] + right[size - 1 + index - i] == 0:
            row[i] = left[index + i] = right[size - 1 + index - i] = 1
            DFS(index + 1)
            row[i] = left[index + i] = right[size - 1 + index - i] = 0


size = int(sys.stdin.readline())
board = [[0] * size for _ in range(size)]
row = [0] * size  # 열
left = [0] * (2 * size - 1)  # 왼쪽 대각선
right = [0] * (2 * size - 1)  # 오른쪽 대각선
count = 0
DFS(0)
print(count)
