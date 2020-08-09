import sys

list_size = int(sys.stdin.readline())
num_list = [list(map(int, sys.stdin.readline().split())) for _ in range(list_size)]

repeat_count = int(sys.stdin.readline())
for _ in range(repeat_count):
    condition = list(map(int, sys.stdin.readline().split()))
    chosen_line = num_list[condition[0] - 1]
    count = 0
    while count != condition[2]:
        if condition[1]:
            pop_num = chosen_line.pop()
            chosen_line.insert(0, pop_num)
        else:
            pop_num = chosen_line.pop(0)
            chosen_line.append(pop_num)
        count += 1
    num_list[condition[0] - 1] = chosen_line

total = 0
for (index, value) in enumerate(num_list):
    if index <= list_size // 2:
        total += sum(value[index:list_size - index])
    else:
        total += sum(value[list_size - index - 1:index + 1])
print(total)
