import sys

# sys.stdin = open("input.txt")

"""
1.이항계수를 만든다
2.순열 전체를 구한다
3.이항계수와 순열에서 각각 index를 곱하고 조건에 맞는지 체크한다
"""


def DFS(index, total):
    global flag, temp, is_zero
    if not flag:
        return
    if index == size and total == require:
        for item in temp:
            print(item, end=" ")
        flag = False
        return
    for j in range(size):
        if is_zero[j] == 0:
            is_zero[j] = 1
            temp[index] = j + 1
            DFS(index + 1, total + (factor[index] * temp[index]))
            is_zero[j] = 0


size, require = map(int, sys.stdin.readline().split())
factor = [1] * size
temp = [0] * size
is_zero = [0] * size
flag = True
for i in range(1, size):
    factor[i] = factor[i - 1] * (size - i) // i
DFS(0, 0)