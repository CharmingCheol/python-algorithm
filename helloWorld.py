"""
[case1]
print("강한친구 대한육군")
print("강한친구 대한육군");
[case2]
print("강한친구 대한육군\n"*2) """

"""
[case1]
a,b = input().split()
print(int(a) + int(b))
[case2]
a,b = input().split()
a = int(a)
b = int(b)
print(a + b)
"""

"""
[case1]
a,b = input().split()
print(int(a/b))
[case2]
a,b = input().split()
print(round(a/b))
"""

"""
a,b = map(int, input().split())
if a < b :
    print("<")
elif a > b :
    print(">")
else:
    print("==")
"""

"""
a = 100
if 90 <= a & a <= 100 :
    print("A")
elif 80 <= a & a <= 89 :
    print("B")
"""

"""
a, b = map(int, input().split())
c = list(map(int, input().split()))
for i in range(a):
    if c[i] < b:
        print(c[i], end=" ")
"""

"""
while True:
    a,b = map(int, input().split())
    if a == 0 & b == 0:
        break
    print(a + b)
"""

"""
while True:
    try:
        a, b = map(int, input().split())
        print(a + b)
    except:
        break
"""

"""
find(=자바의 index와 동일. 원하는 값 없으면 -1 리턴)
"""

"""
*언박싱, 코드 반복
"""
