nums = [False, False] + [True] * 250000
for i in range(2, 250000):
    if nums[i]:
        for j in range(2 * i, 250000, i):
            nums[j] = False
while True:
    count = 0
    N = int(input())
    if N == 0:
        break
    for N in range(N + 1, 2 * N + 1):
        if nums[N]:
            count += 1
    print(count)
