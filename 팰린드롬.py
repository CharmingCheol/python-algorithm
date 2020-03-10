from sys import stdin

word = str(stdin.readline().strip())
arr = [0] * 26
error = 0
result = ""

# 문자열을 알파벳 리스트에 담기
for i in word:
    arr[ord(i) - 65] += 1
# 홀수로 있는 알파벳 갯수 찾기
for i in arr:
    if i % 2 == 1:
        error += 1

if error > 1:
    print("I'm Sorry Hansoo")
else:
    for i in range(len(arr)):
        if arr[i] != 0:
            result += chr(i + 65)
            arr[i] -= 1
    for i in range(len(arr) - 1, -1, -1):
        if arr[i] != 0:
            result += chr(i + 65)
            arr[i] -= 1
    print(result)
