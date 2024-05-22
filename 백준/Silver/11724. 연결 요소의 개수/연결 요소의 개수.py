# https://www.acmicpc.net/problem/11724

import sys
from collections import deque

def BFS(node, graph, visit):
    if visit[node]:
        return False
    nodes = deque([node])
    visit[node] = 0

    while nodes:
        node = nodes.pop()
        for i in range(N):
            if (not visit[i]) and graph[node][i]:
                nodes.append(i)
                visit[i] = 1
    return True

input = sys.stdin.readline
N, M = map(int, input().split())
graph = [[0 for _ in range(N)] for _ in range(N)]
visit = [0 for _ in range(N)]
res = 0

for _ in range(M):
    n1, n2 = map(int, input().split())
    graph[n1 - 1][n2 - 1] = 1
    graph[n2 - 1][n1 - 1] = 1

for node in range(N):
    if BFS(node, graph, visit):
        res += 1

print(res)
