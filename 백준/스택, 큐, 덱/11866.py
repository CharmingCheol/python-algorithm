import sys

arr, eliminate = map(int, sys.stdin.readline().split())
people = [person + 1 for person in range(arr)]
result = []
index = 0
while len(people) != 0:
    for i in range(eliminate):
        if index == len(people):
            index = 0
        if i == eliminate - 1:
            result.append(people.pop(index))
            break
        index += 1
print(result)