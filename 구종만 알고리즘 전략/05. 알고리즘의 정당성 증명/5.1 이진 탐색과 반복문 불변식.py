arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
start = -1
end = len(arr)
standard = 10
while start + 1 < end:
    mid = (start + end) // 2
    if arr[mid] < standard:
        start = mid
    else:
        end = mid
print(end)

"""
전제조건 : arr[start] < standard <= arr[end]
1. 불변식 1
   > while문 내부로 들어왔다는 의미는 start와 end의 차이가 2 이상이라는 의미이므로, mid는 항상 두 값의
     사이에 위치하게 됨
2. 불변식 2
   > arr[mid] < standard인 경우 : 반복문을 시작 할 때 standard < arr[end]라는 건 전제조건.
     arr[mid] < standard < arr[end]이므로, start에 standard를 대입해도 불변식은 성립
   > standard < arr[mid]인 경우 : arr[start] < standard와 합쳐 보면 aarr[start] < standard <= arr[mid]가 되므로,
     불변식이 성립 됨
while문이 종료 될 때 원하는 값은 arr[end]에 저장되어 있음을 알 수 있음
"""
