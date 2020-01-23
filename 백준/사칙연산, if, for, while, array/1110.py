a = int(input())
count = 1
standard = a
while True:
    b = (int(a % 10) * 10) + (int(a / 10 + a % 10) % 10)
    a = b
    if b == standard:
        break
    count += 1
print(count)