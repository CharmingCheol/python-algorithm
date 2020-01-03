arr = [False, False] + [True] * 10000
for a in range(2, len(arr)):
    if arr[a]:
        for b in range(2 * a, len(arr), a):
            arr[b] = False
for i in range(int(input())):
    num = int(input())
    start = num // 2
    end = start
    while True:
        if arr[start] and arr[end]:
            break
        start -= 1
        end += 1
    print(start, end)
