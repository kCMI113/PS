# https://www.acmicpc.net/problem/2579

import sys

input = sys.stdin.readline

n = int(input())
steps = [int(input()) for _ in range(n)]
res = [[0, 0] for _ in range(n + 1)]
res[1] = [steps[0], steps[0]]
for i in range(2, n + 1):
    res[i][0] = steps[i - 1] + max(res[i - 2])
    res[i][1] = steps[i - 1] + res[i - 1][0]

print(max(res[n]))