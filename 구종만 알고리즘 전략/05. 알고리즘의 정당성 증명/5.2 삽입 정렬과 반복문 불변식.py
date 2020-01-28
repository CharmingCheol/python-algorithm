arr2 = [1, 5, 7, 3, 2, 5, 8, 9, 3, 9, 6, 4, 4, 2, 7]
for i in range(len(arr2)):
    # 불변식 a : arr[0...i-1]은 이미 정렬되있다
    index = i
    while index > 0 and arr2[index - 1] > arr2[index]:
        # 불변식 b : arr[index+1...i]의 모든 원소는 arr[index]보다 크다
        # 불변식 c : arr[0...i] 구간은 a[index]를 제외하면 정렬되어 있는 상태이다
        arr2[index - 1], arr2[index] = arr2[index], arr2[index - 1]
        index -= 1
print(arr2)
