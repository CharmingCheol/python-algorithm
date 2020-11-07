import sys

size, pick = map(int, sys.stdin.readline().split())
nums = [index + 1 for index in range(size)]
josephus = []
repeat = 1
cur = 0

while size:
    if repeat == pick:
        josephus.append(nums.pop(cur))
        repeat = 0
        cur -= 1
        size -= 1
    else:
        repeat += 1
        cur += 1
    if size <= cur:
        cur = 0
print(josephus)
