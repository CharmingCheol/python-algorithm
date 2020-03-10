from sys import stdin

students = [
    ["Adrian", 0, 1, 2],
    ["Bruno", 1, 0, 1, 2],
    ["Goran", 2, 2, 0, 0, 1, 1]
]
result = [0] * 3
problems = int(stdin.readline())
answer = str(stdin.readline())

index = 1
count = 0
for i in range(3):
    for j in range(problems):
        if index > len(students[i]) - 1:
            index = 1
        if answer[j] == chr(students[i][index] + 65):
            result[i] += 1
        index += 1
    index = 1
max_ = max(result)
print(max_)
for i in range(len(result)):
    if max_ == result[i]:
        print(students[i][0])