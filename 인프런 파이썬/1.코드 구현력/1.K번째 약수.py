from sys import stdin

num, index = map(int, stdin.readline().split())
count = 0
for i in range(1, num + 1):
    if num % i == 0:
        count += 1
    if count == index:
        print(i)
        break
else:
    print(-1)