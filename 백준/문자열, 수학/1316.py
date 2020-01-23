count = 0
for i in range(int(input())):
    word = str(input())
    if word == ''.join(sorted(word, key=word.find)):
        count += 1
print(count)
