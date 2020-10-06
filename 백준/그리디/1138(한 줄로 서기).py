import sys

size = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
check = [0] * size
result = [1] * size
temp = 1

for num in nums:
    for index in range(size):
        if check[index] == 0:
            num -= 1
        if num < 0 and check[index] == 0:
            result[index] = temp
            check[index] = 1
            break
    temp += 1

for item in result:
    print(item, end=" ")
