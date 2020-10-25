""" 플이과정
1.최장 증가 부분 수열(LIS)
 - 어떤 임의의 수열이 주어질 때, 이 수열에서 몇 개의 수들을 제거해서 부분수열을 만들 수 있다.
 - 이때 만들어진 부분수열 중 오름차순으로 정렬된 가장 긴 수열을 최장 증가 부분 수열이라 한다.
2.예시
 - 3 5 7 9 2 1 4 8라는 수열이 있을 때 LIS는 3 5 7 8이 된다.
 - 5 1 6 2 7 3 8이 있을 때, 1 2 3 8과 5 6 7 8이 LIS가 된다.
3.LIS 구하기 알고리즘(N^2)
 - 반복문을 두번 돌려서 현재 수보다 이전 수가 더 크고,
   현재 dp보다 이전 dp가 더 클경우 현재 dp를 갱신
4.lIS 구하기 알고리즘(N log N)
 - N^2은 앞에 있는 수들을 모두 탐색해야 되기 때문에 불필요한 시간이 발생
 - 이분 탐색으로 불필요한 연산을 최소화(정확히 말하자면 lower bound)
5.출처
https://mygumi.tistory.com/303
https://jins-dev.tistory.com/entry/%EC%B5%9C%EC%A0%81%ED%99%94%EB%90%9C-LISLongest-Increasing-Subsequence-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98%EA%B3%BC-%ED%95%B4-%EC%B0%BE%EA%B8%B0
"""
import sys

sys.stdin = open("input.txt")

size = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
dp = [0] * size
dp[0] = 1

for y in range(1, size):
    temp = 0
    for x in range(y, -1, -1):
        if nums[x] < nums[y] and temp < dp[x]:
            temp = dp[x]
    temp += 1
    dp[y] = temp
print(max(dp))

# size = int(sys.stdin.readline())
# nums = list(map(int, sys.stdin.readline().split()))
#
# dp = [0] * size
# dp[0] = nums[0]
# trace = dict()
# trace[0] = (0, nums[0])
# index = 0
#
# for i in range(1, size):
#     if dp[index] < nums[i]:
#         index += 1
#         dp[index] = nums[i]
#         trace[i] = (index, nums[i])
#     else:
#         start = 0
#         end = index
#         while start < end:
#             mid = (start + end) // 2
#             if dp[mid] >= nums[i]:
#                 end = mid
#             else:
#                 start = mid + 1
#         dp[end] = nums[i]
#         trace[i] = (end, nums[i])
#
#
# stack = []
# temp = index
# for i in range(size - 1, -1, -1):
#     if temp == trace[i][0]:
#         stack.append(trace[i][1])
#         temp -= 1
# print(stack)