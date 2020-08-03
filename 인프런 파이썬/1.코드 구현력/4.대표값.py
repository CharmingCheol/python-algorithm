from sys import stdin

size = int(stdin.readline())
scores = list(map(int, stdin.readline().split()))
average = round(sum(scores) / size)

current_score = scores[0]
current_index = 0
for (index, value) in enumerate(scores):
    if abs(average - current_score) > abs(average - value):
        current_score = value
        current_index = index
    if abs(average - current_score) >= abs(average - value) and current_score < value:
        current_score = value
        current_index = index
print(average, current_index + 1)