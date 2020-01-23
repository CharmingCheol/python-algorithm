mul = 1
arr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for i in range(3):
    mul *= int(input())
while mul >= 1:
    index = int(mul % 10)
    mul /= 10
    arr[index] += 1
for i in range(len(arr)):
    print(arr[i])

"""a = int(input())
b = int(input())
c = int(input())

value = a * b * c
stan = value
arr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

while stan != 0:
    index = int(value % 10)
    value /= 10
    stan = int(value)
    arr[index] += 1

for i in range(len(arr)):
    print(arr[i])
"""