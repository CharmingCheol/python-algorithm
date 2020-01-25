arr = [-7, 4, -3, 6, 3, -8, 3, 4]
sum = 0
result = 0
for i in arr:  # 최댓값 점화식 => result = (max(sum,0) + i), result)
    sum = max(sum, 0) + i
    result = max(sum, result)
print(result)
"""
4.9와 4.11 모두 같은 문제지만 시간 복잡도가 O(N^3), O(N^2), O(N) 각각 다름
"""