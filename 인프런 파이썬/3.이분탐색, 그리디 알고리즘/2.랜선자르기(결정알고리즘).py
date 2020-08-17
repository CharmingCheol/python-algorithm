import sys

size, require = map(int, sys.stdin.readline().split())
flex = []
for _ in range(size):
    flex.append(int(sys.stdin.readline()))

left = 0
right = max(flex) // 2
index = 0
while left <= right:
    mid = (left + right) // 2
    count = 0
    for item in flex:
        count += item // mid
    if count >= require:
        index = mid
        left = mid + 1
    else:
        right = mid - 1
print(index)
