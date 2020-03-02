from sys import stdin

word = str(stdin.readline().strip())
first, second, third = "", "", ""
result = word
arr = []

for i in range(1, len(word) - 1):
    for j in range(i, len(word) - 1):
        first = word[0:i][::-1]
        second = word[i:j + 1][::-1]
        third = word[j + 1:len(word)][::-1]
        arr.append(first + second + third)
print(sorted(arr)[0])