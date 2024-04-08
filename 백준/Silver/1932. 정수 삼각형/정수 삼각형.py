# https://www.acmicpc.net/problem/1932

import sys

n = int(sys.stdin.readline().rstrip())
prev_row = [int(sys.stdin.readline().rstrip())]

for i in range(1, n):
    line = [*(map(int, sys.stdin.readline().rstrip().split()))]
    mid_eles = [max(prev_row[j - 1], prev_row[j]) + line[j] for j in range(1, len(line) - 1)]  # 가운데 원소들
    prev_row = [line[0] + prev_row[0], *mid_eles, line[-1] + prev_row[-1]]  # 왼쪽 끝, 가운데 원소들, 오른쪽 끝

print(max(prev_row))
