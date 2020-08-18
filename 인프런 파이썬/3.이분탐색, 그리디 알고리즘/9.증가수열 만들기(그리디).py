import sys

size = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))

left = 0
right = size - 1
last = 0
result = ""

while left <= right:
    if last < nums[left] and last < nums[right]:
        compare_left_right = nums[left] < nums[right]
        last = nums[left] if compare_left_right else nums[right]
        result += "L" if compare_left_right else "R"
        if compare_left_right:
            left += 1
        else:
            right -= 1
    elif last < nums[left]:
        last = nums[left]
        left += 1
        result += "L"
    elif last < nums[right]:
        last = nums[right]
        right -= 1
        result += "R"
    else:
        break
print(len(result))
print(result)
