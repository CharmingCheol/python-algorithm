# 이진검색
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
lo = 0
hi = len(arr)
x = 7
while lo + 1 < hi:
    mid = (lo + hi) // 2
    if arr[mid] < x:
        lo = mid
    else:
        hi = mid
print(hi)
"""
repeat = int(input())
arr = list(range(1, int(repeat + 1)))
start = 0
end = len(arr)
target = arr[repeat - 1]
count = 0
while start <= end:
    mid = int((start + end) / 2)
    if arr[mid] == target:
        break
    elif arr[mid] < target:
        start = mid + 1
    else:
        end = mid - 1
    count += 1
print(count+1)
"""
