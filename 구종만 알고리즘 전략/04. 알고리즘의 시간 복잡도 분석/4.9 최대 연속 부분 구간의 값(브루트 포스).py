import sys

# 시간 복잡도가 O(N^3)인 경우
arr1 = [-7, 4, -3, 6, 3, -8, 3, 4]
result = 0
for i in range(len(arr1)):
    for j in range(i, len(arr1)):
        sum = 0
        for k in range(i,j):
            sum += arr1[k]
        result = max(result, sum)
print(result)

# 시간 복잡도가 O(N^2)인 경우
arr2 = [-7, 4, -3, 6, 3, -8, 3, 4]
result = 0
for i in range(len(arr2)):
    sum = 0
    for j in range(i, len(arr2)):
        sum += arr2[j]
        result = max(result, sum)
print(result)