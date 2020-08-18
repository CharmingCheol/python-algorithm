import sys

size = int(sys.stdin.readline())
boxes = list(map(int, sys.stdin.readline().split()))
supple = int(sys.stdin.readline())

for _ in range(supple):
    max_index = boxes.index(max(boxes))
    min_index = boxes.index(min(boxes))
    boxes[max_index] -= 1
    boxes[min_index] += 1
print(max(boxes) - min(boxes))
