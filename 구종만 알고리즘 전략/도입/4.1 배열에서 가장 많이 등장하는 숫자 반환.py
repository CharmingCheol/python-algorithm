import time

start = time.time()
arr = [1, 1, 1, 2, 2, 2, 3, 4, 4, 2, 2, 4, 5, 6, 6, 6, 6, 6, 7, 7, 7, 8, 8, 9, 9, 9, 2, 2, 4, 5, 5, 6, 6, 7, 8, 9, 9, 9]
majority = 0
majorityCount = 0
for i in arr:  # 점점 한칸씩 앞으로
    count = 0
    for j in arr:  # 처음부터 끝까지 기준
        if j == i:
            count += 1
    if count > majorityCount:  # 기존 최댓값보다 count 값이 더 클 경우
        majorityCount = count  # 최대 count 값 갱신
        majority = i  # 최댓값 갱신
print(majority)
print("time :", time.time() - start)

"""
알고리즘 수행 시간을 지배하는 것은 반복문이 지대한 영향을 줌.
위에 코드는 반복문이 두개 겹쳐져 있으므로, 수행 시간은 N^2가 됨
"""
