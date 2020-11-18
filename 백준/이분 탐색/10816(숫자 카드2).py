import sys

N = int(sys.stdin.readline())
dic = dict()
for num in list(map(int, sys.stdin.readline().split())):
    if num in dic:
        dic[num] += 1
    else:
        dic[num] = 1
M = int(sys.stdin.readline())
isCard = list(map(int, sys.stdin.readline().split()))

for item in isCard:
    print(dic[item] if item in dic else 0, end=" ")