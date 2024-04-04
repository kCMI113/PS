# https://www.acmicpc.net/problem/9935

import sys

string = list(sys.stdin.readline().rstrip())
bomb = list(sys.stdin.readline().rstrip())
len_bomb = len(bomb)
res = []

for s in string:
    res.append(s)
    if len(res) >= len_bomb and s == bomb[-1]:
        if bomb == res[-len_bomb:]:
            for _ in range(len_bomb):
                res.pop()

if res:
    print(*res, sep="")
else:
    print("FRULA")
