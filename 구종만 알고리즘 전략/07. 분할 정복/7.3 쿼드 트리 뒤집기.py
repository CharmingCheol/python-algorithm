pointer = 0
qt = "xbwxwbbwb"


def reverse():
    global pointer
    # 기저 사례 : 문자열에서 x가 아닐 경우(b나 w일 경우)
    # 현재 위치에 있는 문자열을 리턴함
    if qt[pointer] != "x":
        pointer += 1
        return qt[pointer - 1]
    else:
        pointer += 1
        ul = reverse()
        ur = reverse()
        ll = reverse()
        lr = reverse()
    return "x" + ll + lr + ul + ur


print(reverse())