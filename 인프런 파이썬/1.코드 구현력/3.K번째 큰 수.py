from sys import stdin

size, condition = map(int, stdin.readline().split())
arr = list(map(int, stdin.readline().split()))
result = set()

for i in range(size):
    for j in range(i + 1, size):
        for k in range(j + 1, size):
            result.add(arr[i] + arr[j] + arr[k])
result = list(result)
result.sort(reverse=True)
print(result[condition - 1])