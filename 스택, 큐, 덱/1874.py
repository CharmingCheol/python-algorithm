import sys
arr = []
result = []
standard = 1
for _ in range(int(sys.stdin.readline())):
    num = int(sys.stdin.readline())
    while standard <= num:
        arr.append(standard)
        result.append("+")
        standard += 1
    if arr[-1] == num:
        arr.pop()
        result.append("-")
if not arr:
    for i in result:
        print(i)
else:
    print("NO")