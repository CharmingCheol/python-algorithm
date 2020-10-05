import sys

calc = list(map(str, sys.stdin.readline().split("-")))
nums = []
for item in calc:
    splitPlus = item.split("+")
    temp = 0
    for num in splitPlus:
        temp += int(num)
    nums.append(temp)

result = nums[0]
for index in range(1, len(nums)):
    result -= nums[index]
print(result)
