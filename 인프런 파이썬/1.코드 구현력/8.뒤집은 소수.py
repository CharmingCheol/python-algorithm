import sys

prime_list = [False] * 2 + [True] * 100000
for (index, value) in enumerate(prime_list):
    if value:
        for true_index in range(index * 2, len(prime_list), index):
            prime_list[true_index] = False


# 숫자 뒤집기
def reverse(num):
    return num[::-1].lstrip("0")


# 소수 판별
def isPrime(num):
    return prime_list[int(num)]


size = int(sys.stdin.readline())
num_list = list(map(str, sys.stdin.readline().split()))
result = []
for value in num_list:
    flip_num = reverse(value)
    if isPrime(flip_num):
        result.append(flip_num)
print(" ".join(result))
