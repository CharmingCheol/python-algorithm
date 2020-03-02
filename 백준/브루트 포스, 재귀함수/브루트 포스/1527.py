from sys import stdin


def goldminsoo(num):
    global result
    if num > B:
        return
    if A <= num <= B:
        result += 1
    goldminsoo(num * 10 + 4)
    goldminsoo(num * 10 + 7)


A, B = map(int, stdin.readline().split())
result = 0
goldminsoo(4)
goldminsoo(7)
print(result)