from sys import stdin
import math


def isSatify(a, b):
    brown = b - 2
    red = a * b
    brown = (a - 2) * brown
    red -= brown

    if red == l and brown == w:
        return True
    return False


l, w = map(int, stdin.readline().split())
sum_ = l + w
sqrt_ = int(math.sqrt(sum_))

for a in range(3, sqrt_ + 1):
    b = int(sum_ / a)
    if b <= 2:
        continue
    if a * b == sum_:
        if isSatify(a, b):
            if a > b:
                print(a, b)
            else:
                print(b, a)
"""
r, b = map(int, input().split())
for i in range(3, 2000):
    for j in range(3, i + 1):
        a = (i * 2) + ((j - 2) * 2)
        if a == r and (i * j) - a == b:
            print(i, j)
"""