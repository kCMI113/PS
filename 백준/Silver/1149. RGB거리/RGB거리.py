# https://www.acmicpc.net/problem/1149

import sys

input = sys.stdin.readline

n = int(input())
costs = [list(map(int, input().split())) for _ in range(n)]
totals = [[0, 0, 0] for _ in range(n)]  # RGB
totals[0] = costs[0]

for i in range(0, n):
    totals[i][0] = costs[i][0] + min(totals[i - 1][1], totals[i - 1][2])
    totals[i][1] = costs[i][1] + min(totals[i - 1][0], totals[i - 1][2])
    totals[i][2] = costs[i][2] + min(totals[i - 1][1], totals[i - 1][0])

print(min(totals[n - 1]))
