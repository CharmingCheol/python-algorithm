import sys

# 풀이 1
first_size = int(sys.stdin.readline())
first_num_list = list(map(int, sys.stdin.readline().split()))

second_size = int(sys.stdin.readline())
second_num_list = list(map(int, sys.stdin.readline().split()))

first_num_list.extend(second_num_list)
first_num_list.sort()
for num in first_num_list:
    print(num, end=" ")

# 풀이 2
first_size = int(sys.stdin.readline())
first_list = list(map(int, sys.stdin.readline().split()))

second_size = int(sys.stdin.readline())
second_list = list(map(int, sys.stdin.readline().split()))

first_index = 0
second_index = 0
result = []
while first_index < first_size and second_index < second_size:
    if first_list[first_index] <= second_list[second_index]:
        result.append(first_list[first_index])
        first_index += 1
    else:
        result.append(second_list[second_index])
        second_index += 1
if second_index != second_size:
    result += second_list[second_index:]
elif first_index != first_size:
    result += first_list[first_index:]
for num in result:
    print(num, end=" ")
