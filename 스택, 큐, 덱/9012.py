import sys

for _ in range(int(sys.stdin.readline())):
    word = list(sys.stdin.readline().strip())
    while len(word) != 0:
        if ")" not in word:
            break
        elif word[0] == ')':
            break
        else:
            if word[word.index(')')] == ')':
                word.remove("(")
                word.remove(")")
    print("YES" if len(word) == 0 else "NO")