import sys

n1, n2, n3 = map(int, sys.stdin.readline().split())

if n1 == n2 == n3:
    res = 10000 + n1 * 1000
elif n1 == n2 or n1 == n3:
    res = 1000 + n1 * 100
elif n3 == n2:
    res = 1000 + n3 * 100
else:
    res = max([n1, n2, n3]) * 100

print(res)
