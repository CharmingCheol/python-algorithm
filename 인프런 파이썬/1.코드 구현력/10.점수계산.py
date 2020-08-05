import sys

size = int(sys.stdin.readline())
array = list(map(int, sys.stdin.readline().split()))

additional_score = 0
total = 0
for score in array:
    if score:
        additional_score += 1
        total += additional_score
    else:
        additional_score = 0
print(total)