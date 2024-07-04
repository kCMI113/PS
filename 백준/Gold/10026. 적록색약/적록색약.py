import sys
from collections import deque

input = sys.stdin.readline


def BFS(x, y, graph, lim, visit):
    if visit[x][y]:
        return
    que = deque([[x, y]])
    visit[x][y] = 1
    dx = [0, -1, 0, 1]
    dy = [-1, 0, 1, 0]

    while que:
        now_x, now_y = que.popleft()
        for i in range(len(dx)):
            new_x, new_y = now_x + dx[i], now_y + dy[i]
            if -1 < new_x < lim and -1 < new_y < lim:
                if graph[new_x][new_y] == graph[x][y] and not visit[new_x][new_y]:
                    visit[new_x][new_y] = 1
                    que.append([new_x, new_y])
    return 1


n = int(input())
graph = [list(input()) for _ in range(n)]
visit = [[0] * n for _ in range(n)]
res1, res2 = 0, 0

for c in range(n):
    for r in range(n):
        if BFS(r, c, graph, n, visit):
            res1 += 1

for i in range(n):
    for j in range(n):
        if graph[i][j] == "G":
            graph[i][j] = "R"

visit = [[0] * n for _ in range(n)]
for c in range(n):
    for r in range(n):
        if BFS(r, c, graph, n, visit):
            res2 += 1

print(f"{res1} {res2}")
