import sys

sys.stdin = open("input.txt")

size = int(sys.stdin.readline())
words = [str(sys.stdin.readline().strip()) for _ in range(size)]
alphabet = [0] * 26

# 단어 별 알파벳 가중치 계산
for word in words:
    for (index, text) in enumerate(word):
        alphabet[ord(text) - 65] += 10 ** (len(word) - index - 1)
alphabet.sort(reverse=True)

# 각 알파벳 가중치롤 모두 더하기
result = 0
for index in range(9, -1, -1):
    result += alphabet[9 - index] * index
print(result)
