import sys

timer = int(sys.stdin.readline())
buttons = [300, 60, 10]
temp = [0] * 3

for (index, button) in enumerate(buttons):
    if timer // button:
        temp[index] = timer // button
        timer %= button
if timer:
    print(-1)
else:
    for item in temp:
        print(item, end=" ")
