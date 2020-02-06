import sys


# 브루트 포스로 푼 문제
def bruteForce(h):
    ret = 0
    for left in range(len(h)):
        minHeight = h[left]
        for right in range(left, len(h)):
            minHeight = min(minHeight, h[right])
            ret = max(ret, (right - left + 1) * minHeight)
    return ret


word = list(map(int, sys.stdin.readline().strip().split()))
print(bruteForce(word))


############ 경계선 ############

# 분할 정복으로 푼 문제
def solve(h, left, right):
    global count
    # 기저 사례 : left, right 모두 0일 때(판자가 하나만 존재할 경우), 높이 값 전달
    if left == right == 0:
        return h[left]
    if left == right:
        return h[left - 1]
    # 중앙 인덱스 값 찾기
    mid = (left + right) // 2
    # 중앙 값 기준으로 좌측, 우측 분할 정복
    ret = max(solve(h, left, mid), solve(h, mid + 1, right))

    # 중앙값에 걸쳐있는 사각형 2개 찾기
    lo = mid
    hi = mid + 1
    # 사각형 2개 중에서 높이가 낮은 사각형 찾기
    height = min(h[lo - 1], h[hi - 1])
    # 너비가 2이고 높이가 height인 사각형과 ret 값 중에서 최댓값 찾기
    ret = max(ret, height * 2)

    # 사각형이 입력 전체를 덮을 때 까지 반복. 범위를 넓힐 때 마다 hi 값은 업데이트
    while left + 1 < lo - 1 or hi + 1 < right - 1:
        # 범위가 오른쪽으로 확장하는 경우
        # 왼쪽으로는 가지 못하고 오른쪽 범위가 더 크기 때문에 우측으로 이동
        if hi < right and (lo == left or h[lo - 2] < h[hi]):
            hi += 1
            height = min(height, h[hi - 1])
        # 우측으로 가지 않는 경우엔 좌측으로 이동
        else:
            lo -= 1
            height = min(height, h[lo])
        ret = max(ret, height * (hi - lo + 1))
    return ret


print("배열값 : ", end="")
h = list(map(int, sys.stdin.readline().strip().split()))

print("배열 길이 : ", end="")
length = int(sys.stdin.readline())

print(solve(h, 0, length))
"""
7 1 5 9 6 7 3
1 4 4 4 4 1 1
1 8 2 2
"""