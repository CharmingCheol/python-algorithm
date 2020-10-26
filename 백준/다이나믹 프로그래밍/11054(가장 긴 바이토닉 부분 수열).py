"""
1.패턴 찾기
 - 왼쪽 부분의 증가수열, 오른쪽 부분의 증가수열을 각각 구해준다
 - 두 개의 증가수열을 더해줘서 가장 큰 값을 출력시킨다
"""
import sys

size = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))

toLeft = [0] * size
toRight = [0] * size
result = [0] * size

toLeft[0] = 1
toRight[size - 1] = 1

# 왼쪽 부분 증가 수열 구하기
for y in range(1, size):
    temp = 0
    for x in range(y - 1, -1, -1):
        if nums[x] < nums[y] and temp < toLeft[x]:
            temp = toLeft[x]
    toLeft[y] = temp + 1

# 오른쪽 부분 증가 수열 구하기
for y in range(size - 2, -1, -1):
    temp = 0
    for x in range(y + 1, size):
        if nums[x] < nums[y] and temp < toRight[x]:
            temp = toRight[x]
    toRight[y] = temp + 1

# 양쪽 모두 구한 부분을 더하기
for index in range(size):
    result[index] = toLeft[index] + toRight[index] - 1
print(max(result))