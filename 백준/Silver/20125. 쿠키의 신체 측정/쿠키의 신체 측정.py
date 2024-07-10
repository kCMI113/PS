import sys

input = sys.stdin.readline
N = int(input())
table = [input() for _ in range(N)]
res = [0 for _ in range(7)]  # 머리위치, 심장, 왼팔, 오른팔, 허리, 오른다리, 왼다리
i = 0

while True:
    idx = table[i].find("*")
    i += 1
    if idx > -1:
        res[0] = idx
        res[1] = i
        break

arm_start = table[i].find("*")
arm_cnt = table[i].count("*")
res[2] = idx - arm_start
res[3] = arm_cnt - 1 - res[2]
i += 1

while table[i].count("*") == 1:
    res[4] += 1
    i += 1
while i < N and table[i].count("*") == 2:
    res[5] += 1
    res[6] += 1
    i += 1

lag_idx = table[i].find("*") if i < N else -1
if lag_idx:
    lag = 5 if lag_idx < res[0] else 6
    while i < N and table[i].count("*") == 1:
        res[lag] += 1
        i += 1

print(res[1] + 1, res[0] + 1)
print(*res[2:], sep=" ")