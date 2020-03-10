from sys import stdin

# 123부터 987까지 답이 될 수 없는 경우를 미리 계산
arr = [False] * 122 + [True] * 866
for i in range(123, 988):
    string = str(i)
    if string[0] == string[1] or string[0] == string[2] or string[1] == string[2]:
        arr[i - 1] = False
    if string[2] == "0":
        arr[i - 1] = False

# 위에서 걸리진 숫자에서 답이 아닌 경우 계산
num = int(stdin.readline())
for i in range(num):
    baseball = list(map(int, stdin.readline().strip().split()))
    for j in range(123, 988):
        one = str(baseball[0])
        two = str(j)
        strike_count, ball_count = 0, 0
        for a in range(3):
            for b in range(3):
                if a == b and one[a] == two[b]:
                    strike_count += 1
                if a != b and one[a] == two[b]:
                    ball_count += 1
        if strike_count != baseball[1] or ball_count != baseball[2]:
            arr[j - 1] = False

# True인 경우 카운트
count = 0
for i in range(123, 988):
    if arr[i - 1]:
        count += 1
print(count)
