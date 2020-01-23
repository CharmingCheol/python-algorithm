for i in range(int(input())):
    H = int(input())
    W = int(input())
    arr = [i for i in range(1, W+1)]
    for _ in range(H):
        for a in range(1, W):
            arr[a] += arr[a-1]
    print(arr[W-1])
