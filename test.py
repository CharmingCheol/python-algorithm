import time
now = time.time()
arr = [1, 2, 3, 4, 5, 6, 7]
index = 4
result = 0
for i in range(len(arr)):
    if arr[i] == index:
        result = i
print(-1 if result == 0 else result)
print("time : ", time.time() - now)
