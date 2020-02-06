def pow(A, m):
    # 기저 사례 : 제곱 수가 0이면 배열의 크기를 return
    if m == 0:
        return A
    # 제곱 수를 2로 나눌 때 0이 아닐 경우
    if m % 2 != 0:
        # 짝수 갯수가 분할 정복 되도록 하나를 떼어놓음
        return pow(A, m - 1) * A
    # 제곱 수 분할
    half = pow(A, m / 2)
    return half * half

# 첫번째 값은 배열의 크기(5x5 = 25), 두번째 값은 배열의 제곱 수((5x5)^2 = 625)
print(pow(5, 2))