# https://www.acmicpc.net/problem/2156

import sys

input = sys.stdin.readline
n = int(input())
wine = [int(input()) for _ in range(n)]
res = [[0, 0, 0] for _ in range(n)]  # 한 번 마심, 두 번 마심, 안 마심
res[0][:2] = wine[0], wine[0]

for i in range(1, n):
    res[i][0] = res[i - 1][2] + wine[i]  # 이전에 와인 안 마심 (i가 1번째 와인)
    res[i][1] = res[i - 1][0] + wine[i]  # 이전에 와인 마심 (i가 2번째 와인)
    res[i][2] = max(res[i - 1])  # i 안 마심, 이전 라운드의 최대값

print(max(res[n - 1]))
