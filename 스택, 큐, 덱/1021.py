import sys

create, find = map(int, sys.stdin.readline().split())
findNum = list(map(int, sys.stdin.readline().split()))
numList = [i + 1 for i in range(int(create))]
count = 0
while len(findNum) != 0:
    if numList[0] == findNum[0]:
        numList.pop(0)
        findNum.pop(0)
    else:
        if numList.index(findNum[0]) < len(numList) / 2:
            numList.append(numList.pop(0))
        else:
            numList.insert(0, numList.pop())
        count += 1
print(count)
