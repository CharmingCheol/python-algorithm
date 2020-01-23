for i in range(int(input())):
    repeat, word = input().split()
    result = ''
    for j in word:
        result += j * int(repeat)
    print(result)