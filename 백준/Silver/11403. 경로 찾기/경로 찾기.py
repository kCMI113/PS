# https://www.acmicpc.net/problem/11403

import sys

input = sys.stdin.readline

n = int(input())
adj = [list(map(int, input().split())) for _ in range(n)]

for mid in range(n):
    for i in range(n):
        for j in range(n):
            if adj[i][j] == 1:
                continue
            if adj[i][mid] == 1 and adj[mid][j] == 1:
                adj[i][j] = 1
            else:
                adj[i][j] = 0


for i in range(n):
    print(*adj[i], sep=" ")
