import sys
import heapq

arr = []
while True:
    num = int(sys.stdin.readline())
    if num == -1:
        break
    if num == 0:
        if not arr:
            print(-1)
        else:
            print(heapq.heappop(arr))
    else:
        heapq.heappush(arr, num)
