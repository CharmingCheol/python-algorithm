from sys import stdin

N, M = map(int, stdin.readline().split())
arr = [str(stdin.readline().strip()) for i in range(N)]
result = 0

for i in range(N):
    for j in range(M):
        for k in range(0, min(N, M)):
            if i + k < N and j + k < M and arr[i + k][j] == arr[i][j] and arr[i + k][j + k] == arr[i][j] and arr[i][
                j + k] == arr[i][j]:
                result = max(result, k + 1)
print(result * result)