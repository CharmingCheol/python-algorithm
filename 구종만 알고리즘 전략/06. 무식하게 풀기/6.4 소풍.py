import sys
import numpy as np

print("학생의 수 ", end="")
n = int(sys.stdin.readline())

print("친구 쌍의 수 ", end="")
m = int(sys.stdin.readline())

areFriends = np.array([[False] * 10] * 10)

def countParing(taken):
    # 짝을 찾은 인덱스 계산을 위한 변수 선언
    firstFree = -1
    # 학생 수 만큼 반복
    for i in range(n):
        # i번째 값이 false인 경우(짝이 지어지지 않은 경우)
        if not taken[i]:
            # 해당 인덱스의 값을 짝을 찾을 변수로 변경
            firstFree = i
            # 짝을 지을 학생을 찾았으므로 반복 중지
            break
    # 기저 사례 : 모든 학생이 짝을 찾았으니 종료
    if firstFree == -1:
        return 1
    ret = 0
    for pairWith in range(firstFree + 1, n):
        if (not taken[pairWith]) and (areFriends[firstFree][pairWith]):
            taken[firstFree] = taken[pairWith] = True
            ret += countParing(taken)
            taken[firstFree] = taken[pairWith] = False
    return ret


# 학생을 담을 배열 선언
taken = [False] * 10

# 서로 친구인 학생의 수만큼 반복
for i in range(m):
    print("서로 친구인 학생 입력")
    friend1 = int(sys.stdin.readline())
    friend2 = int(sys.stdin.readline())
    # (a, b), (b, a)는 같은 경우이므로, 둘다 true로 선언
    areFriends[friend1][friend2] = areFriends[friend2][friend1] = True
print(countParing(taken))