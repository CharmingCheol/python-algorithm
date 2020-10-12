import sys

for _ in range(int(sys.stdin.readline())):
    height, width, room = map(int, sys.stdin.readline().split())
    a = room % height
    b = room // height + 1
    if a == 0:
        a = height
        b -= 1
    print(a * 100 + b)
