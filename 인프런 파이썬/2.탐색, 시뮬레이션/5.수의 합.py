import sys

size, result = map(int, sys.stdin.readline().split())
num_list = list(map(int, sys.stdin.readline().split()))

start = 0
end = 1
count = 0
total = num_list[0]
while True:
    if total < result:
        if end < size:
            total += num_list[end]
            end += 1
        else:
            break
    elif total == result:
        total -= num_list[start]
        start += 1
        count += 1
    elif total > result:
        total -= num_list[start]
        start += 1
print(count)
