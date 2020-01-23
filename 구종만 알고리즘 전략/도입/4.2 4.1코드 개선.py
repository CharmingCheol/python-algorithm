import time

start = time.time()
arr = [1, 1, 1, 2, 2, 2, 3, 4, 4, 2, 2, 4, 5, 6, 6, 6, 6, 6, 7, 7, 7, 8, 8, 9, 9, 9, 2, 2, 4, 5, 5, 6, 6, 7, 8, 9, 9, 9]
count = [0] * 10
for i in range(len(arr)):
    count[arr[i]] += 1  # i가 증가하여 arr[0] = 1, arr[1] = 1, arr[2] = 1이 되지만,
                        # count 기준으로는 arr[0~2]까지 모두 1이므로 count[1] = count[arr[0~2]]
majority = 0
for i in range(len(count)):
    if count[i] > count[majority]:  # count i번째가 count 최댓값 보다 클 경우 최댓값을 i 값으로 갱신
        majority = i
print(count)
print(majority)
print("time :", time.time() - start)