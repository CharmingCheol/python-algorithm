from sys import stdin


def calc(x, arr, multiple):
    while x > 0:
        arr[int(x % 10)] += multiple
        x = int(x / 10)


num = int(stdin.readline())
arr = [0] * 10
multiple, start = 1, 1

while start <= num:
    while num % 10 != 9 and start <= num:
        calc(num, arr, multiple)
        num -= 1
    if num < start:
        break
    while num % 10 != 0 and start <= num:
        calc(start, arr, multiple)
        start += 1
    num /= 10
    start /= 10
    for i in range(10):
        arr[i] += int(num - start + 1) * multiple
    multiple *= 10
print(*arr)
