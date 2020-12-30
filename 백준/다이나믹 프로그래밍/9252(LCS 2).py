import sys

S1 = sys.stdin.readline().strip().upper()
S2 = sys.stdin.readline().strip().upper()
len1 = len(S1)
len2 = len(S2)

matrix = [[0] * (len2 + 1) for _ in range(len1 + 1)]
for i in range(1, len1 + 1):
    for j in range(1, len2 + 1):
        if S1[i - 1] == S2[j - 1]:
            matrix[i][j] = matrix[i - 1][j - 1] + 1
        else:
            matrix[i][j] = max(matrix[i - 1][j], matrix[i][j - 1])

arr = []
while matrix[len1][len2] != 0:
    if matrix[len1][len2] == matrix[len1 - 1][len2]:
        len1 -= 1
    elif matrix[len1][len2] == matrix[len1][len2 - 1]:
        len2 -= 1
    elif matrix[len1][len2] == matrix[len1 - 1][len2 - 1] + 1:
        len1 -= 1
        len2 -= 1
        arr.append(S2[len2])
arr.reverse()
print(matrix[-1][-1])
print("".join(arr))
