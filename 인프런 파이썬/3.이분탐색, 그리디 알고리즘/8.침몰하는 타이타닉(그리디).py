import sys

size, standard = map(int, sys.stdin.readline().split())
weight = list(map(int, sys.stdin.readline().split()))
weight.sort(reverse=True)

left = 0
right = size - 1
result = 0

while left <= right:
    if weight[left] + weight[right] <= standard:
        left += 1
        right -= 1
    else:
        left += 1
    result += 1
print(result)