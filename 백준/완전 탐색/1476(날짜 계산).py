import sys

E, S, M = map(int, sys.stdin.readline().split())
e, s, m = 1, 1, 1
count = 1
while True:
    if E == e and S == s and M == m:
        print(count)
        break
    e += 1
    s += 1
    m += 1
    count += 1
    if e == 16:
        e = 1
    if s == 29:
        s = 1
    if m == 20:
        m = 1
