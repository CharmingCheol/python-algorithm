import sys

num = int(sys.stdin.readline())


def fibo(first, second, count):
    if 0 == num:
        return 0
    elif 1 == num:
        return 1
    else:
        sum = first + second
        if count == num:
            return sum
        return fibo(second, sum, count + 1)

print(fibo(0, 1, 2))