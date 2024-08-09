from collections import deque

F, S, G, U, D = map(int, input().split())
graph = [-1 for _ in range(F + 1)]


def BFS(now):
    graph[now] = 0
    que = deque([now])

    while que:
        now = que.popleft()
        if now == G:
            return

        points = [now + U, now - D]
        for p in points:
            if 1 <= p <= F and graph[p] == -1:
                graph[p] = graph[now] + 1
                que.append(p)


BFS(S)
print("use the stairs" if graph[G] == -1 else graph[G])