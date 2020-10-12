import sys

size = 10000
temp = [False] + [True] * size

for index in range(size + 1):
    if temp[index]:
        num = index
        while True:
            num += sum(map(int, str(num)))
            if size < num:
                break
            temp[num] = False
for index in range(size + 1):
    if temp[index]:
        print(index)