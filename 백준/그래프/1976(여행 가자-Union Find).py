import sys


def getParent(x):
    if cities[x] == x: return x
    cities[x] = getParent(cities[x])
    return cities[x]


def unionParent(a, b):
    a = getParent(a)
    b = getParent(b)
    if a < b:
        cities[b] = a
    else:
        cities[a] = b


def findParent(a, b):
    a = getParent(a)
    b = getParent(b)
    return True if a == b else False


def checkResult():
    for i in range(path_count - 1):
        if not findParent(pathArr[i], pathArr[i + 1]):
            return "NO"
    return "YES"


city_count = int(sys.stdin.readline())
path_count = int(sys.stdin.readline())
cities = [i for i in range(city_count + 1)]

for y in range(city_count):
    line = list(map(int, sys.stdin.readline().split()))
    for x in range(city_count):
        if line[x] == 1:
            unionParent(y + 1, x + 1)
pathArr = list(map(int, sys.stdin.readline().split()))
print(checkResult())