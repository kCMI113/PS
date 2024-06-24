import sys
from collections import deque

input = sys.stdin.readline
N = int(input())

graph = [list(map(int, input().split())) for _ in range(N)]
lb = max(min(map(min, graph)) - 1, 0)
ub = max(map(max, graph)) + 1
res = []


def BFS(x, y, lim, t_graph, visit):
    if visit[y][x] or t_graph[y][x] <= lim:
        return 0
    que = deque([[x, y]])
    visit[y][x] = 1
    dx = [0, -1, 0, 1]
    dy = [-1, 0, 1, 0]

    while que:
        now_x, now_y = que.popleft()
        for i in range(4):
            new_x, new_y = now_x + dx[i], now_y + dy[i]
            if -1 < new_x < N and -1 < new_y < N:
                if t_graph[new_y][new_x] > lim and (not visit[new_y][new_x]):
                    visit[new_y][new_x] = 1
                    que.append([new_x, new_y])
    return 1


for lim in range(lb, ub):
    temp_graph = graph
    visit = [[0 for _ in range(N)] for _ in range(N)]
    temp_res = 0
    for col in range(N):
        for row in range(N):
            if BFS(col, row, lim, temp_graph, visit):
                temp_res += 1

    res.append(temp_res)

print(max(res))
