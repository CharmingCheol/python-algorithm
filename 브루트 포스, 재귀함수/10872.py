import sys

num = int(sys.stdin.readline())


def factorial(factorial_num):
    if factorial_num == 1:
        return 1
    return factorial_num * factorial(factorial_num - 1)


print(factorial(num))
