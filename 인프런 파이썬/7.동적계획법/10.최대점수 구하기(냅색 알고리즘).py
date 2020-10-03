import sys

kind, time = map(int, sys.stdin.readline().split())
nums = []
for _ in range(kind):
    nums.append(list(map(int, sys.stdin.readline().split())))

dp = [0] * (time + 1)

for y in range(1, kind + 1):
    (question_score, question_time) = nums[y - 1]
    for x in range(time, question_time - 1, -1):
        dp[x] = max(dp[x], dp[x - question_time] + question_score)
print(dp[time])
