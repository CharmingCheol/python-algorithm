number = int(input())
result = 0
while number > 0:
    if number == 1 or number == 2 or number == 4 or number == 7:
        result = -1
        break
    else:
        if number % 5 == 0:
            number -= 5
        else:
            number -= 3
        result += 1
print(result)
