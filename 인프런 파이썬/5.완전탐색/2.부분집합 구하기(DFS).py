import sys

size = int(sys.stdin.readline())
temp = [0] * (size + 1)


def recursive(num):
    if num == size + 1:
        for (index, item) in enumerate(temp):
            if item == 1:
                print(index, end=" ")
        return print()
    else:
        temp[num] = 1
        recursive(num + 1)
        temp[num] = 0
        recursive(num + 1)


recursive(1)
