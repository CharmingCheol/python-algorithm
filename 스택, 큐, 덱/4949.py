import sys

while True:
    word = list(sys.stdin.readline())
    if word[0] == ".":
        break
    else:
        compare = [i for i in word if "[" in i or "]" in i or "(" in i or ")" in i]
        while True:
            if len(compare) == 0:
                break
            elif compare[0] == ")" or compare[0] == "]":
                break
            elif "(" in compare and compare[compare.index("(")] == "(":
                if ")" not in compare:
                    break
                elif compare[compare.index(")")] == ")":
                    compare.remove(")")
                    compare.remove("(")
            elif "[" in compare and compare[compare.index("[")] == "[":
                if "]" not in compare:
                    break
                elif compare[compare.index("]")] == "]":
                    compare.remove("]")
                    compare.remove("[")
        print("yes" if len(compare) == 0 else "no")