import sys

calc = str(sys.stdin.readline())
stack = []
for item in calc:
    if item.isdecimal():
        stack.append(item)
    else:
        temp = eval(stack.pop(-2) + item + stack.pop(-1))
        stack.append(str(temp))
print(int(stack[0]))
