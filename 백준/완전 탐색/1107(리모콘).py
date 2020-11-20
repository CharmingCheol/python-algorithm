import sys


def flag(index):
    num = list(str(index))
    for item in num:
        if item in breakDown:
            return False
    return True


target = int(sys.stdin.readline())
size = int(sys.stdin.readline())
breakDown = list(map(str, sys.stdin.readline().split()))
count = abs(target - 100)

for index in range(1000001):
    if flag(index):
        count = min(count, len(str(index)) + abs(index - target))
print(count)
