import sys

sys.stdin = open("input.txt")

size, tape = map(int, sys.stdin.readline().split())
loc = list(map(int, sys.stdin.readline().split()))
loc.sort()
temp = loc[0]
count = 1

for index in range(1, size):
    if temp + tape - 1 < loc[index]:
        temp = loc[index]
        count += 1
print(count)