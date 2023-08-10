import sys
from collections import deque

def dfs(node: int) -> None:
    if visit[node]:
        return
    
    print(node, end=" ")
    visit[node] = 1

    for next in adj_matrix[node]:
        dfs(next)

def bfs(node: int) -> None:
    que = deque([node])
    print(node, end=" ")
    visit[node] = 1

    while que:
        now = que.popleft()
        for next in adj_matrix[now]:
            if not visit[next]:
                que.append(next)
                visit[next] = 1
                print(next, end=" ")

N, M, V = map(int, sys.stdin.readline().rstrip().split())
adj_matrix = [[] for _ in range(N+1)]


for _ in range(M):
    a,b = map(int, sys.stdin.readline().rstrip().split())
    adj_matrix[a].append(b)
    adj_matrix[b].append(a)
    adj_matrix[a].sort()
    adj_matrix[b].sort()


visit = [0 for _ in range(N+1)]
dfs(V)
print('')

visit = [0 for _ in range(N+1)]
bfs(V)