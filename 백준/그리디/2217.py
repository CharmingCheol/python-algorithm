import sys

sys.stdin = open("input.txt")

size = int(sys.stdin.readline())
rope = [int(sys.stdin.readline()) for _ in range(size)]
rope.sort()

result = 0
for index in range(size):
    result = max(result, rope[index] * (size - index))
print(result)

"""
- 10, 15 로프 2개가 있을 때 10 로프는 10을 들 수 있고, 15 로프는 15를 들 수 있음
- 그런데 10, 15를 둘다 사용할 때는 w/k이므로, w가 20 이상이면 10 로프는 버티지 못함
- 즉, 연결한 로프 중 가장 최소 로프 무게 * 연결한 로프 수를 곱하면 됨
"""