from sys import stdin

num = int(stdin.readline())
if num < 100:
    print(num)
else:
    count = 99
    for i in range(100, num + 1):
        aa = list(map(int, str(i)))
        if aa[0] - aa[1] == aa[1] - aa[2]:
            count += 1
    print(count)
