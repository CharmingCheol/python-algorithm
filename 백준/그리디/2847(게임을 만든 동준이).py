import sys

size = int(sys.stdin.readline())
score = [int(sys.stdin.readline()) for _ in range(size)]
score.reverse()
temp = score[0]
result = 0

for index in range(1, size):
    if score[index] < temp:
        temp = score[index]
    else:
        result += score[index] - temp + 1
        temp -= 1
    if temp <= 0:
        temp = 1
print(result)