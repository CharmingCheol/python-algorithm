import sys

# 풀이 1
limit = int(sys.stdin.readline())
words = []
turn = 0
while turn < limit * 2 - 1:
    word = str(sys.stdin.readline().strip())
    if word in words:
        words.pop(words.index(word))
    else:
        words.append(word)
    turn += 1
print(words[0])

# 풀이 2
limit = int(sys.stdin.readline())
words = dict()
for _ in range(limit):
    word = str(sys.stdin.readline().strip())
    words[word] = 1
for _ in range(limit - 1):
    word = str(sys.stdin.readline().strip())
    words[word] = 0
for (key, value) in words.items():
    if value:
        print(key)
        break
