num = 10
result = 0
# 반복 함수
for i in range(1, num+1):
    result += i
print(result)

# 재귀 함수
def recursiveSum(num):
    if num == 1:  # 더 이상 쪼개지지 않는 최소한의 작업에 도달했을 때, 답을 반호나하는 조건문을 포함해야 함
        return 1
    return num + recursiveSum(num-1)
print(recursiveSum(num))
