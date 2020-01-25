import time
start = time.time()
n = 100000
if n == 1:
    print(1)
else:
    ret = []
    for i in range(2, n):
        while n % i == 0:
            n /= i
            ret.append(i)
    print(ret)
print(time.time()-start)