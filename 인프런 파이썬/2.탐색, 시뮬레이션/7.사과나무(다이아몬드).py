import sys

size = int(sys.stdin.readline())
total = 0
for index in range(size):
    num_list = list(map(int, sys.stdin.readline().split()))
    divided_half = size // 2
    if index <= size // 2:
        total += sum(num_list[divided_half - index:divided_half + index + 1])
    else:
        total += sum(num_list[index - divided_half:size + divided_half - index])
print(total)
