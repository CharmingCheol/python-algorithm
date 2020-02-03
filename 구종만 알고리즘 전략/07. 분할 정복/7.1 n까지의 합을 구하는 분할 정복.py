def fastSum(number):
    if number == 1:
        return 1
    if number % 2 == 1:
        return fastSum(number - 1) + number
    return 2 * fastSum(number / 2) + (number / 2) * (number / 2)


print(int(fastSum(6)))

"""
1. 분할정복
   > 전체를 2등분씩 나누고, 홀수 갯수인 경우 하나를 떨어트려서 다시 2등분으로 나눔.
     기저 사례가 나올 때 까지 이를 반복
   > 일반적인 재귀함수보다 진행 횟수가 더 적음
2. n까지 수열의 합을 구할 때
   > 1.func(num) = (1+2+...+(1/2)) + ((n/2+1)+(n/2+2)+...+(n/2+n/2))
   > 2.func(num/2)을 하면 앞에 있는 수식인 (1+2+...+(1/2)) 부분만 해당되기에 뒤에 있는 수식을 구해줘야 함
   > 3.((n/2+1)+(n/2+2)+...+(n/2+n/2)) = n/2 + n/2 + (1+2+...+n/2)과 같음
   > 4.(1+2+...+n/2)은 func(num/2)과 같으니, func(num)을 점화식으로 표현한다면,
       func(num) = (n/2+1)+(n/2+2) + 2 * func(num/2)가 됨
   > 5.홀수인 경우에는 n-1까지의 합을 재귀 호출로 계산하고 n을 더해줌
"""
