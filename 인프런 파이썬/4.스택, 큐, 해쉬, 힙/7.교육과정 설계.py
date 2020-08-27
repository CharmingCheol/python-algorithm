import sys

limit = str(sys.stdin.readline().strip())
for index in range(int(sys.stdin.readline())):
    extract = ""
    for item in str(sys.stdin.readline().strip()):
        if item in limit and not item in extract:
            extract += item
    if extract[:len(limit)] == limit:
        print("#%d %s" % (index + 1, "YES"))
    else:
        print("#%d %s" % (index + 1, "NO"))