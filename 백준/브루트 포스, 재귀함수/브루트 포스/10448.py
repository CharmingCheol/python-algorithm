from sys import stdin

triangle = [int(i * (i + 1) / 2) for i in range(1, 100)]
eureka = [0] * 1001

for i in triangle:
    for j in triangle:
        for k in triangle:
            if i + j + k <= 1000:
                eureka[i + j + k] = 1

repeat = int(stdin.readline())
for _ in range(repeat):
    print(eureka[int(stdin.readline())])