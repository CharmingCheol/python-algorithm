import sys

for _ in range(int(sys.stdin.readline())):
    n, r = list(map(int, sys.stdin.readline().split()))
    denominator = 1  # 분모
    numerator = 1  # 분자
    # n!
    for i in range(r):
        numerator *= (i + 1)
    # (r - n)!
    for i in range(r - n):
        denominator *= (i + 1)
    # n!
    for i in range(n):
        denominator *= (i + 1)
    print(numerator // denominator)
