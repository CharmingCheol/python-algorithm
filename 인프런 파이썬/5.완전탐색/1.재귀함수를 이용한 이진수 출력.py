import sys


def recurvise(num):
    if num == 1:
        return "1"
    else:
        if num % 2:
            return recurvise(num // 2) + "1"
        else:
            return recurvise(num // 2) + "0"


result = recurvise(int(sys.stdin.readline()))
print(result)
