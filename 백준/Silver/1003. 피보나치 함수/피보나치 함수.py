# https://www.acmicpc.net/problem/1003

import sys

case = int(sys.stdin.readline().rstrip())
cnt_0 = [1, 0]
cnt_1 = [0, 1]


for _ in range(case):
    n = int(sys.stdin.readline().rstrip())
    if len(cnt_0) < n + 1:
        for i in range(len(cnt_0), n + 1):
            cnt_0.append(cnt_0[i - 1] + cnt_0[i - 2])
            cnt_1.append(cnt_1[i - 1] + cnt_1[i - 2])
    print(cnt_0[n], cnt_1[n], sep=" ")
