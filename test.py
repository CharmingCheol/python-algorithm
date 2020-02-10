from sys import stdin

repeat = int(stdin.readline())
arr = list(map(int, stdin.readline().split()))
add, sub, mul, div = map(int, stdin.readline().split())
max_, min_ = -1e9, 1e9


def calc(num, res, add, sub, mul, div):
    global max_, min_
    if num == repeat:
        max_ = max(max_, res)
        min_ = min(min_, res)
        return
    else:
        if add:
            calc(num + 1, res + arr[num], add - 1, sub, mul, div)
        if sub:
            calc(num + 1, res - arr[num], add, sub - 1, mul, div)
        if mul:
            calc(num + 1, res * arr[num], add, sub, mul - 1, div)
        if div:
            calc(num + 1, res // arr[num], add, sub, mul, div - 1)


calc(1, arr[0], add, sub, mul, div)
print(max_)
print(min_)