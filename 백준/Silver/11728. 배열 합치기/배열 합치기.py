import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
res = []
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a_idx, b_idx = 0, 0

while len(res) < n + m:
    if a[a_idx] <= b[b_idx]:
        res.append(a[a_idx])
        a_idx += 1
    else:
        res.append(b[b_idx])
        b_idx += 1
    if a_idx >= n:
        res += b[b_idx:]
        break
    if b_idx >= m:
        res += a[a_idx:]
        break

print(*res, sep=" ")
