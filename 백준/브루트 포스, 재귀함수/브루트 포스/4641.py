from sys import stdin

while True:
    numbers = list(map(int, stdin.readline().strip().split()))
    count = 0
    if numbers[0] == -1:
        break
    for i in numbers:
        for j in numbers:
            if i == j * 2 and i != j:
                count += 1
    print(count)