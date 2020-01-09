import sys
for _ in range(int(sys.stdin.readline())):
    word = list(sys.stdin.readline().strip())
    repeat = int(sys.stdin.readline())
    if repeat == 0:
        input_arr = sys.stdin.readline().strip()
        input_arr = []
    else:
        input_arr = list(map(int, input()[1:-1].split(',')))
    boolFlag = False
    for i in word:
        if i == "R":
            input_arr.reverse()
        elif i == "D":
            if not input_arr:
                boolFlag = True
                break
            else:
                input_arr.pop(0)
    print("error" if boolFlag else input_arr)
