import sys

# 풀이 1
line = str(sys.stdin.readline().strip())
extract_num = list(filter(lambda word: str.isdigit(word), line))
num = int("".join(extract_num).lstrip("0"))
count = 0
for index in range(1, num + 1):
    if num % index == 0:
        count += 1
print(num, count, sep="\n")

# 풀이 2
s = input()
res = 0
for x in s:
    if x.isdecimal():
        res = res * 10 + int(x)
print(res)
cnt = 0
for i in range(1, res + 1):
    if res % i == 0:
        cnt += 1
print(cnt)
