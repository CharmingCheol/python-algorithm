day, night, meter = map(int, input().split())
standard = (meter - night) / (day-night)
print(int(standard) if standard == int(standard) else int(standard)+1)

""" 시간초과 1
day, night, meter = map(int, input().split())
result = 1
current = 0
while True:
    if current + day == meter:
        break
    current += (day-night)
    result += 1
print(result)"""

""" 시관초과 2
day, night, meter = map(int, input().split())
result = 1
current = 0
while True:
    if current < meter:
        if current + day == meter:
            break
        current += (day-night)
        result += 1
    else:
        break
print(result)"""
