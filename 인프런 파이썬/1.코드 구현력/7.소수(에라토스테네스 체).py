import sys

size = int(sys.stdin.readline())
array = [False] * 2 + [True] * (size - 1)
for (index, item) in enumerate(array):
    if item:
        for trueIndex in range(2 * index, len(array), index):
            array[trueIndex] = False
print(array.count(True))