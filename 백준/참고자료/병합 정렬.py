def merge(left, right):
    result = []
    while len(left) > 0 or len(right) > 0:
        if len(left) > 0 and len(right) > 0:
            if left[0] <= right[0]:
                result.append(left[0])
                left = left[1:]
            else:
                result.append(right[0])
                right = right[1:]
        elif len(left) > 0:
            result.append(left[0])
            left = left[1:]
        elif len(right) > 0:
            result.append(right[0])
            right = right[1:]
    return result

def merge_sort(data):
    if len(data) <= 1:
        return data
    mid = len(data) // 2
    left = data[:mid]
    right = data[mid:]
    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left, right)

data_list = [8, 5, 9, 3, 1, 6, 7, 2, 4]
print(data_list)
print(merge_sort(data_list))
