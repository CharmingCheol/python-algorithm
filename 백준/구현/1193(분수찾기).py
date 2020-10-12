import sys

num = int(sys.stdin.readline())
maxLine = 0
maxValue = 0

while maxValue < num:
    maxLine += 1
    maxValue += maxLine

if maxLine % 2 == 1:
    up = maxValue - num + 1
    down = maxLine + 1 - up
    print("%d/%d" % (up, down))
else:
    down = maxValue - num + 1
    up = maxLine + 1 - down
    print("%d/%d" % (up, down))