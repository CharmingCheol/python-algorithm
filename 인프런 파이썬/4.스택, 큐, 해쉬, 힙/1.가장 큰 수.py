import sys

nums, limit = map(int, sys.stdin.readline().split())
count = 0
result = []

for item in str(nums):
    while True:
        if not result:
            result.append(item)
            break
        elif item <= result[-1]:
            result.append(item)
            break
        elif count == limit:
            result.append(item)
            break
        else:
            result.pop()
            count += 1
for item in result[0:len(str(nums)) - limit]:
    print(item, end="")