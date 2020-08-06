import sys

# 풀이 1
num_array = [num for num in range(1, 21)]
for _ in range(10):
    start, end = map(int, sys.stdin.readline().split())
    flip = num_array[start - 1:end]
    flip.reverse()
    num_array[start - 1:end] = flip
print(" ".join(map(str, num_array)))

# 풀이 2
a = list(range(21))
for _ in range(10):
    s, e = map(int, input().split())
    for i in range((e - s + 1) // 2):
        a[s + i], a[e - i] = a[e - i], a[s + i]
a.pop(0)
for x in a:
    print(x, end=" ")
