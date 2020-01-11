import sys

Q = [i + 1 for i in range(int(sys.stdin.readline()))]
while len(Q) != 1:
    Q.pop(0)
    Q.append(Q.pop(0))
print(*Q)
