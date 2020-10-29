"""
1.패턴 찾기
 - 높이가 1인 경우
    > nums[0]을 출력시킨다
 - 높이가 2인 경우
    > nums[0] + nums[1]을 출력시킨다
    > 한칸씩 올라온 경우이기 때문
 - 높이가 3이상인 경우
    > case1 = nums[index] + nums[index - 1] + dp[index - 3]
      case2 = nums[index] + dp[index - 2]
      dp[index] = max(case1, case2)
"""
import sys

size = int(sys.stdin.readline())
nums = list(int(sys.stdin.readline()) for _ in range(size))
dp = [0] * size
dp[0] = nums[0]

if size == 1:
    print(nums[0])
elif size == 2:
    print(nums[0] + nums[1])
else:
    for index in range(1, 3):
        case1 = nums[index - 1] + nums[index]  # 이전 계단 + 현재 계단
        case2 = nums[index]  # 현재 계단
        if index == 2:
            case2 += nums[index - 2]  # 전전계단
        dp[index] = max(case1, case2)

    for index in range(3, size):
        # 현재 + 이전 계단 + 전전전계단 dp 값
        case1 = nums[index] + nums[index - 1] + dp[index - 3]
        # 현재 + 전전계단 dp값
        case2 = nums[index] + dp[index - 2]
        dp[index] = max(case1, case2)
    print(dp[size - 1])
