from sys import stdin

for i in range(int(stdin.readline())):
    size, start, end, index = map(int, stdin.readline().split())
    num_list = list(map(int, stdin.readline().split()))[start - 1:end]
    num_list.sort()
    print("#%d %d" % (i+1, num_list[index - 1]))