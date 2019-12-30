# https://www.acmicpc.net/problem/10817

a,b,c = map(int, input().split())
list = [a,b,c]
list.sort()
print(list[1])