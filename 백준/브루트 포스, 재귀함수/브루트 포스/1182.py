from sys import stdin


def result(index, add):
    global count
    if index == repeat:
        return
    if add + arr[index] == standard:
        count += 1
    result(index + 1, add + arr[index])
    result(index + 1, add)


repeat, standard = map(int, stdin.readline().split())
arr = list(map(int, stdin.readline().split()))
count = 0
result(0, 0)
print(count)

"""
def result(index, add):
    global count
    if index >= repeat:
        if add == standard:
            count += 1
            return
        return
    result(index + 1, add + arr[index])
    result(index + 1, add)


repeat, standard = map(int, stdin.readline().split())
arr = list(map(int, stdin.readline().split()))
count = 0
result(0, 0)
print(count - 1 if standard == 0 else count)
"""