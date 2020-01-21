import sys
num = int(sys.stdin.readline().strip())
result = 0
for a in range(int(num)):
     sum_num = sum(list(map(int, str(a)))) + int(a)
     if sum_num == num:
         result = a
         break
print(result)