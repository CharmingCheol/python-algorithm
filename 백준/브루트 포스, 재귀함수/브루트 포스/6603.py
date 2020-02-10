from sys import stdin

arr = list(map(int, stdin.readline().split()))
lottoList = [None] * 6


def pick(depth, num):
    # 기저 사례 : 길이가 6이 되면 리턴
    if depth == 6:
        print(lottoList)
        return
    for i in range(num, arr[0]):
        lottoList[depth] = arr[i + 1]
        pick(depth + 1, i + 1)
        # lottoList[depth] -= 1


"""
https://dongyeollee.github.io/2018/09/23/Al/6603/
"""

pick(0, 0)