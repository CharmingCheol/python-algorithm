import sys

size = int(sys.stdin.readline())
num_list = list(map(str, sys.stdin.readline().split()))

stash_sum = -1
stash_num = -1

for item in num_list:
    total = sum(list(map(int, item)))
    if stash_sum < total:
        stash_sum = total
        stash_num = item
print(stash_num)
