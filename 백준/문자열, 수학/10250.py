for i in range(int(input())):
    H, W, room = map(int, input().split())
    arr = []
    for a in range(W):
        for b in range(H):
            arr.append((b + 1) * 100 + (a + 1))
    print(arr[room-1])

""" 방법2
for _ in range(int(input())):
    H, W, N = map(int, input().split())
    count = 0
    stop = False
    result = 0
    for w in range(W):
        for h in range(H):
            count += 1
            if count == N:
                stop = True
                result = (h + 1) * 100 + (w + 1)
                break
        if stop == True:
            break
    print(result)
"""