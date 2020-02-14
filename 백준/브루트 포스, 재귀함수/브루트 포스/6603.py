from sys import stdin


def lotto(index, result):
    if len(result) == 6:
        return print(*result)
    for i in range(index, arr[0] + 1):
        result.append(arr[i])
        lotto(i + 1, result)
        result.pop(-1)


while True:
    arr = list(map(int, stdin.readline().split()))
    if arr[0] != 0:
        lotto(1, [])
        print()
    else:
        break

"""
https://dongyeollee.github.io/2018/09/23/Al/6603/
"""
