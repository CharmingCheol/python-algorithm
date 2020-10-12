import sys

monthList = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
dayList = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
year = 2007
month, day = map(int, sys.stdin.readline().split())

# 전년도까지의 날수 계산. 윤년을 포함하여 계산
preYear = year - 1
numOfDays = preYear * 365 + int(preYear / 4 - preYear / 100 + preYear / 400)

# 입력받은 월 전까지의 날수를 추가
for index in range(0, month - 1):
    numOfDays += monthList[index]

# 입력받은 년도가 윤년이고, 3월 이상인 경우 날수에 1을 추가
if 3 <= month and (year % 4 == 0 and year % 100 != 0 or year % 400 == 0):
    numOfDays += 1

# 입력받은 일까지 추가
numOfDays += day

# 계산이 끝났으니 7로 나눈 나머지를 계산
dayOfWeek = numOfDays % 7
print(dayList[dayOfWeek])