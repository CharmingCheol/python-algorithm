import sys

while True:
    sentence = sys.stdin.readline().rstrip()
    stack = []
    if sentence == ".": break
    for i in sentence:
        if i == "[" or i == "(":
            stack.append(i)
        elif i == "]":
            if len(stack) == 0:
                stack = -1
                break
            elif stack.pop() != "[":
                stack = -1
                break
        elif i == ")":
            if len(stack) == 0:
                stack = -1
                break
            elif stack.pop() != "(":
                stack = -1
                break
    print("yes" if not stack else "no")

""" 시간 초과
while True:
    sentence = sys.stdin.readline().rstrip()
    if sentence == ".":
        break
    extract = [i for i in sentence if "(" in i or ")" in i or "[" in i or "]" in i]
    boolFlag = False
    while len(extract) != 0:
        first = extract[0]
        if first == ")" or first == "]" or boolFlag:
            break
        if "[" in extract and extract[extract.index("[")] == "[" and extract[extract.index("[") + 1] == ")":
            break
        if "(" in extract and extract[extract.index("(")] == "(" and extract[extract.index("(") + 1] == "]":
            break
        elif first == "(":
            if ")" in extract:
                extract.remove("(")
                extract.remove(")")
            else:
                boolFlag = True
        elif first == "[":
            if "]" in extract:
                extract.remove("[")
                extract.remove("]")
            else:
                boolFlag = True
    print("yes" if not extract else "no")
"""
