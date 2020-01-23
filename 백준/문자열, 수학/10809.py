word = str(input())
result = []
for i in list(map(chr, range(97, 123))):
    if word.find(i) == -1:
        result.append(-1)
    else:
        result.append(word.find(i))
print(*result)
