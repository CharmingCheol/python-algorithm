""" 문제풀이
1.패턴 찾기
 - 첫번째 잔
    > 무조건 마신다
 - 두번째 잔
    > 첫번째 잔도 마시고 두번째 잔도 마신다
 - 세번째 잔
    > 현재 잔을 마시지 않는다(=첫번째 잔, 두번째 잔만 마신다)
    > 현재 잔을 마시고, 이전 잔도 마신다
    > 현재 잔을 마시고, 이전 잔을 마시지 않는다(=첫번째 잔을 마신다)
    > 그 중에서 최댓값으로 할당한다
2.index = 2, index = 3 분기처리를 한 이유?
 - index = 2에서 dp[index - 3]을 하게 되면 index - 3이 음수가 되기 때문에
3.점화식
 - index == 1 => dp[1] = nums[0] + nums[1]
 - index == 2 => dp[2] = max(dp[index - 1],
                             nums[index] + dp[index - 2],
                             nums[index] + nums[index - 1]
                         )
 - index == 3 => dp[index] = max(dp[index - 1],
                                 nums[index] + dp[index - 2],
                                 nums[index] + nums[index - 1] + dp[index - 3]
                             )
"""

import sys

size = int(sys.stdin.readline())
nums = [int(sys.stdin.readline()) for _ in range(size)]

dp = [0] * size
dp[0] = nums[0]

for index in range(1, size):
    case1 = dp[index - 1]  # 현재 잔을 마시지 않은 경우
    case2 = nums[index] + dp[index - 2]  # 이번 잔을 마시고, 이전 잔은 마시지 않은 경우
    if index == 1:
        dp[1] = nums[0] + nums[1]  # 현재 잔을 마시고, 이전 잔도 마신 경우
    elif index == 2:
        case3 = nums[index] + nums[index - 1]  # 현재 잔을 마시고, 이전 잔도 마신 경우
        dp[2] = max(case1, case2, case3)
    else:
        case3 = nums[index] + nums[index - 1] + dp[index - 3]  # 현재 잔을 마시고, 이전 잔도 마신 경우
        dp[index] = max(case1, case2, case3)
print(dp[size - 1])