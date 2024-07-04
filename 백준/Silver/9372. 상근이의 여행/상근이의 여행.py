import sys

input = sys.stdin.readline


def DFS(graph, node, visit, res):
    visit[node] = 1
    for n in graph[node]:
        if not visit[n]:
            res = DFS(graph, n, visit, res + 1)
    return res


N = int(input())
for i in range(N):
    r, c = map(int, input().split())
    graph = [[] for _ in range(r)]
    visit = [0] * r
    for _ in range(c):
        a, b = map(int, input().split())
        graph[a - 1].append(b - 1)
        graph[b - 1].append(a - 1)

    print(DFS(graph, 0, visit, 0))
