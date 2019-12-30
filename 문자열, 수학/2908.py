arr = list(map(str, input().split()))
for i in range(len(arr)):
    arr[i] = "".join(reversed(arr[i]))
print(max(arr))

# arr = list(map(int, input().split()))
# for i in range(len(arr)):
#     one = int(arr[i] % 10)
#     ten = int((arr[i] % 100) / 10)
#     hundred = int(arr[i] / 100)
#     arr[i] = one * 100 + ten * 10 + hundred
# print(max(arr))
