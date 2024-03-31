# https://www.acmicpc.net/problem/1406

import sys

L_stack = list(sys.stdin.readline().rstrip())
R_stack = []
n_inst = int(sys.stdin.readline().rstrip())

for i in range(n_inst):
    inst = sys.stdin.readline().rstrip().split()
    match inst[0]:
        case "L":
            if L_stack:
                R_stack.append(L_stack.pop())
        case "D":
            if R_stack:
                L_stack.append(R_stack.pop())
        case "B":
            if L_stack:
                L_stack.pop()
        case "P":
            L_stack.append(inst[1])

L_stack.extend(reversed(R_stack))
print("".join(L_stack))
