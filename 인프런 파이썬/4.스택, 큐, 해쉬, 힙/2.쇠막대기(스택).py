import sys

metal = list(str(sys.stdin.readline()))
stack = []
count = 0
for index in range(len(metal)):
    if metal[index] == "(":
        stack.append("(")
    else:
        stack.pop()
        if metal[index - 1] == "(":
            count += len(stack)
        else:
            count += 1
print(count)
