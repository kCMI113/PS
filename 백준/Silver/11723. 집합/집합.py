# https://www.acmicpc.net/problem/11650

import sys

n = int(sys.stdin.readline())
res = {str(k): 0 for k in range(1, 21)}
all_set = {str(k): 1 for k in range(1, 21)}
empty_set = {str(k): 0 for k in range(1, 21)}

for _ in range(n):
    inputs = list(sys.stdin.readline().split())
    match inputs[0]:
        case "add":
            if not res[inputs[1]]:
                res[inputs[1]] = 1
        case "remove":
            if res[inputs[1]]:
                res[inputs[1]] = 0
        case "check":
            print(res[inputs[1]])
        case "toggle":
            if not res[inputs[1]]:
                res[inputs[1]] = 1
            else:
                res[inputs[1]] = 0
        case "all":
            res = all_set.copy()
        case "empty":
            res = empty_set.copy()
