# https://www.acmicpc.net/problem/2753
a = 2000
if a % 400 == 0 | (a % 4 == 0 & a % 100 != 0):
    print(1)
else:
    print(0)