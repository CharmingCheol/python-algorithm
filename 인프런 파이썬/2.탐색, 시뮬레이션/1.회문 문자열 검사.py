import sys

for index in range(int(sys.stdin.readline())):
    word = str(sys.stdin.readline().strip().lower())
    flip = word[::-1]
    equal = "YES" if word == flip else "NO"
    print("#%d %s" % (index + 1, equal))
