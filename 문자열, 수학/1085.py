a, b, c, d = map(int, input().split())
print(min(a, b, c - a, d - b))

"""
a, b, c, d = map(int, input().split())
arr = [0, 0, a, b, c, d]
result = []
for i in range(2, len(arr)):
    result.append(arr[i]-arr[i-2])
print(min(result))
"""
