import sys

def dfs(node:int, pre_depth:int) -> None:
    if depth[node]>0:
        return
    
    depth[node] = pre_depth + 1
    
    if node == query:
        return

    for next in adj_matrix[node]:
        dfs(next, depth[node])

N = int(sys.stdin.readline().rstrip())
start, query = map(int, sys.stdin.readline().rstrip().split())
M = int(sys.stdin.readline().rstrip())
adj_matrix = [[] for _ in range(N+1)]

for _ in range(M):
    a,b = map(int, sys.stdin.readline().rstrip().split())
    adj_matrix[a].append(b)
    adj_matrix[b].append(a)

depth = [-1 for _ in range(N+1)]
dfs(start, depth[start])
print(depth[query])