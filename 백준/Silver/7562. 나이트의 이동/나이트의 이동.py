import sys
from collections import deque

input = sys.stdin.readline
T = int(input())


def BFS(x, y, end_x, end_y, graph, l):
    graph[x][y] = 0
    que = deque([])
    que.append([x, y])
    dx = [-2, -1, 1, 2, 2, 1, -1, -2]  # clockwise
    dy = [1, 2, 2, 1, -1, -2, -2, -1]

    while que:
        now_x, now_y = que.popleft()

        if now_x == end_x and now_y == end_y:
            print(graph[now_x][now_y])
            return

        for i in range(len(dx)):
            new_x = now_x + dx[i]
            new_y = now_y + dy[i]
            if 0 <= new_x < l and 0 <= new_y < l and graph[new_x][new_y] == -1:
                que.append([new_x, new_y])
                graph[new_x][new_y] = graph[now_x][now_y] + 1


for _ in range(T):
    l = int(input())
    graph = [[-1 for _ in range(l)] for _ in range(l)]  # -1: not visited
    x, y = map(int, input().split())
    end_x, end_y = map(int, input().split())
    BFS(x, y, end_x, end_y, graph, l)
