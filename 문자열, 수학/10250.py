for i in range(int(input())):
    H, W, room = map(int, input().split())
    arr = []
    for a in range(W):
        for b in range(H):
            arr.append((b + 1) * 100 + (a + 1))
    print(arr[room-1])