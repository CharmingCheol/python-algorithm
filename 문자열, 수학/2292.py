num = int(input())
plus = 0
start = 1
room = 1
if num == 1:
    print(room)
else:
    while True:
        plus = plus + 6
        start = start + plus
        room += 1
        if num <= start:
            print(room)
            break

""" 시간 초과
num = int(input())
start = 1
multi = 0
count = 0
while True:
    i = 1
    count += 1
    for i in range(start + 1, start + 1 + (multi * 6)):
        if num == i:
            break
    if num == i:
        break
    start = start + (multi * 6)
    multi += 1
print(count)"""

""" 런타임 에러
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
print(count+1)"""
