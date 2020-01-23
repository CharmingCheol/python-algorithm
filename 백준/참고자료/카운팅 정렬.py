import sys

def counting_sort(A, k):
    B = [-1] * len(A)
    C = [0] * (k + 1)

    for a in A:
        C[a] += 1

    for i in range(k):
        C[i + 1] += C[i]

    for j in reversed(range(k)):
        B[C[A[j]] - 1] = A[j]
        C[A[j]] -= 1

    return B

data_list = []
for i in range(int(sys.stdin.readline().strip())):
    data_list.append(int(sys.stdin.readline().strip()))
for i in counting_sort(data_list, len(data_list)):
    print(i)