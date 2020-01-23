import sys
read = sys.stdin.readline
stack = []

def push(x):
    stack.append(x)
def pop():
    if not stack:
        print(-1)
    else:
        print(stack.pop())
def size():
    print(len(stack))
def empty():
    if not stack:
        print(1)
    else:
        print(0)
def top():
    if not stack:
        print(-1)
    else:
        print(stack[-1])

N = int(read())

for i in range(N):
    a = read().split()
    if a[0] == 'top':
        top()
    elif a[0] == 'size':
        size()
    elif a[0] == 'empty':
        empty()
    elif a[0] == 'pop':
        pop()
    elif a[0] == 'push':
        push(a[1])