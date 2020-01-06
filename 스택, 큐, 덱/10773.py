import sys

stack = []


def push(aa):
    stack.append(aa)


def pop():
    stack.pop()


read = sys.stdin.readline()
for i in range(int(read)):
    num = int(sys.stdin.readline())
    if num == 0:
        pop()
    else:
        push(num)
print(sum(stack))