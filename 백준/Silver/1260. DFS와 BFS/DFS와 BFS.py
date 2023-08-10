import sys
from collections import deque

def dfs(node: int) -> None:
    if visit[node]:
        return
    
    dfs_res.append(node)
    visit[node] = 1

    for next in adj_matrix[node]:
        dfs(next)

def bfs(node: int) -> None:
    que = deque()
    que.append(node)
    bfs_res.append(node)
    visit[node] = 1

    while que:
        now = que.popleft()
        for next in adj_matrix[now]:
            if not visit[next]:
                que.append(next)
                visit[next] = 1
                bfs_res.append(next)

N, M, V = map(int, sys.stdin.readline().rstrip().split())
adj_matrix = [[] for _ in range(N+1)]
dfs_res = []
bfs_res = []

for _ in range(M):
    a,b = map(int, sys.stdin.readline().rstrip().split())
    adj_matrix[a].append(b)
    adj_matrix[b].append(a)
    adj_matrix[a] = sorted(adj_matrix[a])
    adj_matrix[b]= sorted(adj_matrix[b])


visit = [0 for _ in range(N+1)]
dfs(V)
print(" ".join(map(str, dfs_res)))

visit = [0 for _ in range(N+1)]
bfs(V)
print(" ".join(map(str, bfs_res)))