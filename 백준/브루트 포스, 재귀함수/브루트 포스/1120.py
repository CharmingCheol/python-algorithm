from sys import stdin

A, B = map(str, stdin.readline().split())
result = 1e9

for i in range(len(B) - len(A) + 1):
    Min = 0
    for j in range(len(A)):
        if A[j] != B[j + i]:
            Min += 1
    result = min(Min, result)
print(result)