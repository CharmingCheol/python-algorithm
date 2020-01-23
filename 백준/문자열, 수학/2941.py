arr = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
word = str(input())
for i in arr:
    if word.find(i) != -1:
        word = word.replace(i, "0")
print(len(word))