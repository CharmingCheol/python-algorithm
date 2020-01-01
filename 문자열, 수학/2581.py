arr = []
for i in range(int(input()), int(input()) + 1):
    count = 0
    for j in range(2, i + 1):
        if 2 == count:
            break
        if i % j == 0:
            count += 1
    if count == 1:
        arr.append(i)
if len(arr) == 0:
    print(-1)
else:
    print(sum(arr))
    print(min(arr))
