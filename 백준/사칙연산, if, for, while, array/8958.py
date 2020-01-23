R = int(input())
for i in range(R):
    OX = list(map(str, input()))
    sum = 0
    count = 0
    for j in range(len(OX)):
        if OX[j] == "O":
            count += 1
            sum += count
        else:
            count = 0
    print(sum)
