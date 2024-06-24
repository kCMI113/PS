import sys

input = sys.stdin.readline
n = int(input())
res = 0

for _ in range(n):
    alphas = []
    word = input()
    flag = 1
    for c in word:
        if c not in alphas:
            alphas.append(c)
            continue
        if alphas[-1] != c:
            flag = 0
            break
    if flag:
        res += 1

print(res)
