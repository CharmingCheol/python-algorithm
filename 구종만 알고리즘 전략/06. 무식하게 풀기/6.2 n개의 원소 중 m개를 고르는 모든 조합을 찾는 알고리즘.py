# 반복문으로 문제를 해결 할 때
from pprint import pprint

array = []
n = 7
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            for l in range(k + 1, n):
                array.append([i, j, k, l])
pprint(array[:5])


# 재귀 함수로 문제를 해결 할 때
"""
n: 전체 원소의 수
picked: 지금까지 고른 원소들의 번호
to_pick: 더 고를 원소의 수
"""
def pick(n, picked, toPick):
    # 기저 조건 : 더 고를 원소가 없을 때 배열에 담긴 수를 출력
    if toPick == 0:
        print(picked)
        return
    smallest = 0 if not picked else picked[-1] + 1
    for i in range(smallest, n):
        picked.append(i)
        pick(n, picked, toPick - 1)
        picked.pop(-1)


pick(7, [], 4)


"""
1. 반복문으로 문제를 해결 할 때
   > 고르는 숫자의 범위가 4개에서 5개로 변하면 for문을 추가해야 되고, 6개, 7개일 경우에도 계속 for문을 추가해야 됨
   > for문이 중첩된다면 코드는 복잡하고 길어지며, 근본적으로 동적인 코드를 구사하지 못함
2. 재귀함수로 문제를 해결 할 때
   > 재귀함수를 통해 이러한 문제를 유연하고 간결하게 작성 할 수 있음
   > 위 코드에서는 원소들의 총 개수, 원소들을 담는 배열, 더 진행되야 할 횟수를 고려해야 함
"""