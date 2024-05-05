# https://www.acmicpc.net/problem/10844

import sys

input = sys.stdin.readline
n = int(input())
steps = [[0 for _ in range(10)] for _ in range(n)]
steps[0][1:] = [1 for _ in range(9)]

for i in range(1, n):
    steps[i][0] = steps[i - 1][1]
    steps[i][9] = steps[i - 1][8]
    for j in range(1, 9):
        steps[i][j] = steps[i - 1][j - 1] + steps[i - 1][j + 1]

print(sum(steps[n - 1]) % 1000000000)
