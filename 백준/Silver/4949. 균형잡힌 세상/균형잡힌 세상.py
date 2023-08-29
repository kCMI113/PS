import sys

while True:
    stack = []
    total = sys.stdin.readline().rstrip()

    if total == ".":
        break

    for ele in total:
        if ele == '[' or ele == '(':
            stack.append(ele)
        elif ele == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(ele)
                break
        elif ele == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(ele)
                break
        
    if stack:
        print("no")
    else:
        print("yes")