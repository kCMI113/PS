import sys
from collections import deque

def bfs(node:int):
    que = deque([node])
    visit[node] = 1

    while que:
        now = que.popleft()
        for next in adj_matrix[now]:
            if not visit[next]:
                que.append(next)
                visit[next] = 1

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
adj_matrix = [[] for _ in range(N+1)]
visit = [0 for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    adj_matrix[a].append(b)
    adj_matrix[b].append(a)

bfs(1)
print(sum(visit)-1)