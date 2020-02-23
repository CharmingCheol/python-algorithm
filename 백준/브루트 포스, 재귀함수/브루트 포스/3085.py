from sys import stdin


def candy():
    result = 1
    for i in range(num):
        count = 1
        for j in range(1, num):
            if arr[i][j] == arr[i][j-1]:
                count += 1
            else:
                result = max(result, count)
                count = 1
        result = max(result, count)
    for i in range(num):
        count = 1
        for j in range(num - 1):
            if arr[j + 1][i] == arr[j][i]:
                count += 1
            else:
                result = max(result, count)
                count = 1
        result = max(result, count)
    return result


num = int(stdin.readline())
arr = [list(map(str, stdin.readline().strip())) for _ in range(num)]
result = 0

for i in range(num):
    for j in range(num - 1):
        arr[i][j], arr[i][j + 1] = arr[i][j + 1], arr[i][j]
        result = max(result, candy())
        arr[i][j], arr[i][j + 1] = arr[i][j + 1], arr[i][j]

        arr[j + 1][i], arr[j][i] = arr[j][i], arr[j + 1][i]
        result = max(result, candy())
        arr[j + 1][i], arr[j][i] = arr[j][i], arr[j + 1][i]
print(result)