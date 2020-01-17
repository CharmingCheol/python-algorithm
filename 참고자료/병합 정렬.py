def merge(arr, first, middle, last):
    tmp = []
    i, j = first, middle + 1

    while i <= middle and j <= last:
        if arr[i] <= arr[j]:
            tmp.append(arr[i])
            i += 1
        else:
            tmp.append(arr[j])
            j += 1

    while i <= middle:
        tmp.append(arr[i])
        i += 1
    while j <= last:
        tmp.append(arr[j])
        j += 1

    for x in tmp:
        arr[first] = x;
        first += 1

def merge_sort(arr, first, last):
    if first < last:
        middle = (first + last) // 2
        merge_sort(arr, first, middle)
        merge_sort(arr, middle + 1, last)
        merge(arr, first, middle, last)

def m_sort(arr, size):
    merge_sort(arr, 0, size - 1)
    return arr

data_list = [8, 5, 9, 3, 1, 6, 7, 2, 4]
print(data_list)
print(m_sort(data_list, len(data_list)))