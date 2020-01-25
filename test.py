import time

num = 10
result = []
if num == 1:
    print(1)
else:
    for i in range(2, num):
        while num % i == 0:
            num /= i
            result.append(i)
print(result)
"""
배열을 주고 이동 평균을 5로 구해보시오
단, 예시로 5개의 값이 있을 때, 2~5번째 값은 이전과 동일함.
그래서 첫번째 값은 빼고 새로운 값만 추가하면 중복을 방지 할 수 있음
"""
