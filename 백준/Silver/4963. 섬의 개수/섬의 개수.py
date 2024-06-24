import sys
from collections import deque

input = sys.stdin.readline


def BFS(x, y, graph, x_lim, y_lim):
    if not graph[x][y]:
        return
    que = deque([[x, y]])
    graph[x][y] = 0
    dx = [0, -1, 0, 1, -1, 1, -1, 1]
    dy = [-1, 0, 1, 0, 1, 1, -1, -1]

    while que:
        now_x, now_y = que.popleft()
        for i in range(len(dx)):
            new_x, new_y = now_x + dx[i], now_y + dy[i]
            if -1 < new_x < x_lim and -1 < new_y < y_lim:
                if graph[new_x][new_y]:
                    graph[new_x][new_y] = 0
                    que.append([new_x, new_y])
    return 1


while True:
    col, row = map(int, input().split())
    if col == 0 and row == 0:
        break
    graph = [list(map(int, input().split())) for _ in range(row)]
    res = 0
    for c in range(col):
        for r in range(row):
            if BFS(r, c, graph, row, col):
                res += 1
    print(res)
