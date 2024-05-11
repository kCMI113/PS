# https://www.acmicpc.net/problem/1012

import sys

sys.setrecursionlimit(1000000)


def DFS(x, y):
    if not graph[y][x]:
        return 0

    graph[y][x] = 0
    dx = [0, -1, 0, 1]
    dy = [-1, 0, 1, 0]
    for i in range(4):
        new_x, new_y = x + dx[i], y + dy[i]
        if -1 < new_x < m and -1 < new_y < n:
            DFS(new_x, new_y)
    return 1


input = sys.stdin.readline
t = int(input())

for _ in range(t):
    n_bug = 0
    m, n, k = map(int, input().split())  # col, row, k
    graph = [[0 for _ in range(m)] for _ in range(n)]
    for _ in range(k):
        x, y = map(int, input().split())
        graph[y][x] = 1
    for col in range(m):
        for row in range(n):
            if DFS(col, row):
                n_bug += 1
    print(n_bug)
