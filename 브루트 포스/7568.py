import sys
people_info = []
result = []
for _ in range(int(sys.stdin.readline())):
    tall, height = map(int, sys.stdin.readline().split())
    people_info.append([tall,height])
for a in people_info:
    rank = 1
    for b in people_info:
        if a[0] < b[0] and a[1] < b[1]:
           rank += 1
    result.append(rank)
print(*result)