import sys
for _ in range(int(sys.stdin.readline())):
    create, find = map(int, sys.stdin.readline().split())
    numList = [i + 1 for i in range(int(create))]
    priority = list(map(int, sys.stdin.readline().split()))
    findNum = numList[find]
    count = 0
    while True:
        if priority[0] == max(priority):
            if findNum == numList[0]:
                count += 1
                break
            numList.pop(0)
            priority.pop(0)
            count += 1
        else:
            numList.append(numList.pop(0))
            priority.append(priority.pop(0))
    print(count)