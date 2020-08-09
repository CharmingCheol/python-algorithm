import sys

size = int(sys.stdin.readline())
num_list = [list(map(int, sys.stdin.readline().split())) for _ in range(size)]

num_list.insert(0, [0] * size)
num_list.append([0] * size)
for line in num_list:
    line.insert(0, 0)
    line.append(0)

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]
count = 0
for first_index in range(1, len(num_list) - 1):
    for second_index in range(1, len(num_list) - 1):
        current_area = num_list[first_index][second_index]
        if all(current_area > num_list[first_index + dx[point]][second_index + dy[point]] for point in range(4)):
            count += 1
print(count)
