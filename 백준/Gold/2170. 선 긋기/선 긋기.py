# https://www.acmicpc.net/problem/2170

import sys

input = sys.stdin.readline
n = int(input())
res = 0
lines = [list(map(int, input().split())) for _ in range(n)]
lines.sort(key=lambda x: x[0])
left, right = lines[0]

for line in lines:
    if right < line[0]:
        res += abs(right - left)
        left, right = line
    if line[0] <= right < line[1]:
        right = line[1]

res += abs(right - left)
print(res)
