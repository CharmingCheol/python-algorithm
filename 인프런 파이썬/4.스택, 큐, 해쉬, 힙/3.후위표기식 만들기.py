import sys

calc = str(sys.stdin.readline())
stack = []
result = ""
for item in calc:
    if item.isdecimal():
        result += item
    else:
        if item == "(":
            stack.append(item)
        elif item == "*" or item == "/":
            while stack and (stack[-1] == "*" or stack[-1] == "/"):
                result += stack.pop()
            stack.append(item)
        elif item == "+" or item == "-":
            while stack and stack[-1] != "(":
                result += stack.pop()
            stack.append(item)
        elif item == ")":
            while stack[-1] != "(":
                result += stack.pop()
            stack.pop()
while stack:
    result += stack.pop()
print(result)
