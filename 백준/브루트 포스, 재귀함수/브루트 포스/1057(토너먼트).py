import sys

size, kim, lim = map(int, sys.stdin.readline().split())
count = 0

if size < kim or size < lim:
    print(-1)
else:
    while kim != lim:
        kim = kim // 2 + 1 if kim % 2 else kim // 2
        lim = lim // 2 + 1 if lim % 2 else lim // 2
        count += 1
    print(count)
