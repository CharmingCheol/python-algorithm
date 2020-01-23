import sys

for _ in range(int(sys.stdin.readline())):
    word = list(map(str, sys.stdin.readline().strip()))
    while len(word) != 0:
        if word[0] == ")" or not "(" in word or not ")" in word:
            break
        elif word[0] == "(":
            if ")" in word:
                word.remove(")")
                word.remove("(")
    print("YES" if not word else "NO")
