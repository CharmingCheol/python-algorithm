import sys

sys.stdin = open("input.txt")

num = int(sys.stdin.readline())
temp = [0] * (num + 2)
temp[1] = 1
temp[2] = 2

for index in range(3, num + 2):
    temp[index] = temp[index - 2] + temp[index - 1]
print(temp[num + 1])