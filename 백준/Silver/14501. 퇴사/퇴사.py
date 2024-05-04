# https://www.acmicpc.net/problem/14501
import sys

input = sys.stdin.readline

n = int(input())
T = []
P = []
res = [0 for _ in range(n)]
TP = [list(map(int, input().split())) for _ in range(n)]

for i in range(n - 1, -1, -1):
    if TP[i][0] + i > n:
        res[i] = 0
        continue
    if TP[i][0] + i == n:
        res[i] = TP[i][1]
        continue
    res[i] = max(res[i + TP[i][0] :]) + TP[i][1]

print(max(res))
