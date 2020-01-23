import sys
from collections import Counter

arr = []
result = []
for _ in range(int(sys.stdin.readline())):
    arr.append(int(sys.stdin.readline().strip()))
arr.sort()

# 평균
result.append(round(sum(arr) / len(arr)))

# 중앙값
result.append(arr[len(arr) // 2])

# 최빈값
count = Counter(arr).most_common()
if len(count) == 1:
    result.append(count[0][0])
elif count[0][1] == count[1][1]:
    result.append(count[1][0])
else:
    result.append(count[0][0])

# 최대 최소값 크기
result.append(abs(max(arr) - min(arr)))

# 결과
for i in result:
    print(i)
