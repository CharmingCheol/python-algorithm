import sys
arr = []
for _ in range(int(sys.stdin.readline())):
    num = int(sys.stdin.readline().strip())
    if num == 0:
        arr.pop()
    else:
        arr.append(num)
print(sum(arr))