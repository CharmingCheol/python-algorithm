# a : 임대료, 급여 같은 고정 비용
# b : 노트북을 생산하는 재료비, 인건비 같은 가변비용
# a = 1000, b = 70 한대 생산비는 1070원 10대 생산비는 1700원

a, b, c = map(int, input().split())
result = 0
if c <= b:
    result = -1
else:
    result = int(a // (c - b)) + 1
print(result)
