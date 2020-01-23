num_list = int(input())
result = []
for i in range(num_list):
    cnt = 0
    if i == 1:
        continue
    for j in range(2, i + 1):
        if i % j == 0:
            cnt += 1
    if cnt == 1:
        result.append(i)
print(result)