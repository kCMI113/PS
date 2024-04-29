# https://www.acmicpc.net/problem/9095

import sys

input = sys.stdin.readline

n = int(input())
res = [0, 1, 2, 4]  # init
test_case = [int(input()) for _ in range(n)]

for i in range(4, max(test_case) + 1):
    res.append(res[i - 3] + res[i - 2] + res[i - 1])

print(*[res[i] for i in test_case], sep="\n")
