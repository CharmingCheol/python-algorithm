from sys import stdin

num = int(stdin.readline())
index = 1
result = 0

while index <= num:
    result += num - index + 1
    index *= 10
print(result)