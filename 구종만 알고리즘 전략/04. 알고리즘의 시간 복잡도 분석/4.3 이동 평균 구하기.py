A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
ret = []
month = 5
for i in range(month-1, len(A)): # month가 5일 경우 4번째~배열의 길이까지 반복
    partialSum = 0
    for j in range(month):
        partialSum += A[i - j]  # A[4] + A[3] + A[2] + A[1] + A[0] // A[5] + A[4] + A[3] + A[2] + A[1]
    ret.append(partialSum / month)
print(ret)

