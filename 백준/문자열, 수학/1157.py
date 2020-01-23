word = input().upper()
arr = [0] * 26
for i in word:
    arr[ord(i) - 65] += 1
maxIndex = arr.index(max(arr))
arr.sort()
print("?" if arr[25] == arr[24] else chr(maxIndex + 65))