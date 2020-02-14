from sys import stdin

people = int(stdin.readline())
arr = []
for _ in range(people):
    arr.append(list(map(int, stdin.readline().split())))
team = [i for i in range(people)]
start_, link_ = 0, 0
result = 1e9


def calcStart(start):
    global start_
    for i in start:
        for j in start:
            if i != j:
                start_ += arr[i][j]
    return start_


def calcLink(link):
    global link_
    for i in link:
        for j in link:
            if i != j:
                link_ += arr[i][j]
    return link_


def start_link(start, link, index, toPick):
    global start_, link_, result
    if toPick == 0:
        # link 배열 값 추가
        for i in team:
            if not i in start:
                link.append(i)
        # start_ 값 구하기
        calcStart(start)
        # link_값 구하기
        calcLink(link)
        result = min(result, abs(start_ - link_))
        start_, link_ = 0, 0
        return
    for i in range(index, people):
        start.append(i)
        start_link(start, link, i + 1, toPick - 1)
        start.pop(-1)
        # link 값 초기화
        link = []


start_link([], [], 0, int(people / 2))
print(result)