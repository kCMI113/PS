import sys

N = int(sys.stdin.readline())
res = 1

while N > 0:
    if N == 1:
        res = 1
        break
    if N % 2 != 0:
        res = 0
        break
    N /= 2

print(res)
