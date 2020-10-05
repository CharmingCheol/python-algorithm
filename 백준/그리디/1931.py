import sys

size = int(sys.stdin.readline())
rooms = [list(map(int, sys.stdin.readline().split())) for _ in range(size)]
rooms = sorted(rooms, key=lambda room: (room[1], room[0]))
temp = rooms[0][1]
result = 1

for index in range(1, size):
    (start, end) = rooms[index]
    if temp <= start:
        temp = end
        result += 1
print(result)

"""
1.정렬 기준
- 정렬 기준은 끝나는 시간으로 오름차순 정렬을 한다.
- 회의를 빨리 시작해도 회의시간이 늦게 끝난다면, 그 동안에 다른 회의를 진행할 수 없음
- 그래서 회의가 빨리 끝날수록 더 많은 회의실을 이용할 수 있음
2.예시
0 10, 3 4, 2 3, 1 2
- 시작시간 기준 오름차순 정렬
  > 0 10, 1 2, 2 3, 3 4
- 종료시간 기준 내림차순 정렬
  > 1 2, 2 3, 3 4, 0 10
3.시작 시간 = 종료 시간
- 종료시간이 같은 시간이 있다면, 그때는 시작시간이 빠른 기준으로 정렬해야 됨
- 만약 (2, 2), (1, 2) 테이블이 있다면 (1, 2)이 앞에 있어야 2번 가능하기 때문에, 이때는 시작 시간으로 정렬
4.결론
- 1. 먼저 종료 시간 기준으로 오름차순 2. 종료시간이 같다면 시작 시간으로 오름차순 정렬
"""
