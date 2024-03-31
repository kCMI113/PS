# https://www.acmicpc.net/problem/1074

import sys

N, r, c = map(int, sys.stdin.readline().rstrip().split())
cnt = 0

while N:
    N -= 1  # 중앙기준

    if r < 2**N and c < 2**N:  # 좌상
        cnt += 0
    if r < 2**N and c >= 2**N:  # 우상
        cnt += 2 ** (2 * N)
        c -= 2**N
    if r >= 2**N and c < 2**N:  # 좌하
        cnt += (2 ** (2 * N)) * 2
        r -= 2**N
    if r >= 2**N and c >= 2**N:  # 우하
        cnt += (2 ** (2 * N)) * 3
        c -= 2**N
        r -= 2**N
    
print(cnt)