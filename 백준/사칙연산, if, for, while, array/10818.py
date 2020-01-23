Case = int(input())
num_list = list(map(int, input().split()))
print('{} {}'.format(min(num_list), max(num_list)))

"""
N = int(input())
arr = list(map(int, input().split()))
arr.sort()
print(arr[0], end=" ")
print(arr[N-1])
"""