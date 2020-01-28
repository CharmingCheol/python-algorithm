arr = [1, 5, 7, 3, 2, 5, 8, 9, 3, 9, 6, 4, 4, 2, 7]
for i in range(len(arr)):
    minIndex = i
    for j in range(i + 1, len(arr)):
        if arr[minIndex] > arr[j]:
            minIndex = j
    arr[i], arr[minIndex] = arr[minIndex], arr[i]
print(arr)