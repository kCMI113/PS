# https://www.acmicpc.net/problem/1932

import sys

n = int(sys.stdin.readline().rstrip())
res = [[int(sys.stdin.readline().rstrip())]]

for i in range(1, n):
    line = list(map(int, sys.stdin.readline().rstrip().split()))
    temp = []
    for j in range(len(line)):
        left, right = 0, 0
        if j - 1 >= 0:
            left = res[i - 1][j - 1]
        if j < i:
            right = res[i - 1][j]
        temp.append(max(left, right) + line[j])
    res.append(temp)

print(max(res[-1]))
