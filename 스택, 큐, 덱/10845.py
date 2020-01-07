import sys

queue = []
for _ in range(int(sys.stdin.readline())):
    enter = (sys.stdin.readline().split())
    word = enter[0]
    if word == "push":
        queue.append(enter[1])
    elif word == "pop":
        if not queue:
            print(-1)
        else:
            print(queue.pop(-len(queue)))
    elif word == "size":
        print(len(queue))
    elif word == "empty":
        if not queue:
            print(1)
        else:
            print(0)
    elif word == "front":
        if not queue:
            print(-1)
        else:
            print(queue[-len(queue)])
    elif word == "back":
        if not queue:
            print(-1)
        else:
            print(queue[-1])