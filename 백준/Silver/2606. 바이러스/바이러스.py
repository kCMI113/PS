import sys

def dfs(node:int):
    if visit[node]:
        return
    
    visit[node] = 1

    for next in adj_matrix[node]:
        dfs(next)

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
adj_matrix = [[] for _ in range(N+1)]
visit = [0 for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    adj_matrix[a].append(b)
    adj_matrix[b].append(a)

dfs(1)
print(sum(visit)-1)