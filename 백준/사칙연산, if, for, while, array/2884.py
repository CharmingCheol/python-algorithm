# https://www.acmicpc.net/problem/2884
a, b = map(int, input().split())
c = 60 * a + b
a = int((c-45) / 60)
b = int((c-45) % 60)
print(a, b)