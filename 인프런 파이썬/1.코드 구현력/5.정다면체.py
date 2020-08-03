from sys import stdin
from collections import Counter

first_size, second_size = map(int, stdin.readline().split())
dice_first = [i for i in range(1, first_size + 1)]
dice_second = [i for i in range(1, second_size + 1)]
stash = []
for first in dice_first:
    for second in dice_second:
        stash.append(first + second)

result = []
current_frequency = 0
for (value, frequency) in Counter(stash).most_common():
    if current_frequency <= frequency:
        current_frequency = frequency
        result.append(value)
    if current_frequency > frequency:
        break
print(" ".join(map(str, result)))