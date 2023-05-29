import sys
sys.setrecursionlimit(1000000)

N = int(sys.stdin.readline())
nodes = [[] for _ in range(N+1)]
visit = [0 for _ in range(N+1)]
parents = [0 for _ in range(N+1)]

for i in range(N-1):
    fst, snd = list(map(int, sys.stdin.readline().split()))
    nodes[fst].append(snd)
    nodes[snd].append(fst)


def dfs(i:int):
    if visit[i]:
        return
    visit[i] = 1

    for num in nodes[i]:
        if not visit[num]:
            parents[num] = i
            dfs(num)

for i in range(1,N+1):
    dfs(i)

print(*parents[2:], sep='\n')