arr = list(map(int, input().split()))
if arr == [1, 2, 3, 4, 5, 6, 7, 8]:
    print("ascending")
elif arr == [8, 7, 6, 5, 4, 3, 2, 1]:
    print("descending")
else: print("mixed")

"""
arr = list(map(int, input().split()))
index = 0;
for i in range(len(arr)):
    if arr[i] == (i + 1):
        index = 0
    elif arr[i] == len(arr) - i:
        index = 1
    else:
        index = 2

if index == 0:
    print("ascending")
elif index == 1:
    print("descending")
else:
    print("mixed")
"""
