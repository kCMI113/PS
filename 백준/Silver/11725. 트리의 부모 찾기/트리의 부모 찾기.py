import sys
sys.setrecursionlimit(1000000)

N = int(sys.stdin.readline())
nodes = [[] for _ in range(N+1)]
visit = [0 for _ in range(N+1)]
parents = [0 for _ in range(N+1)]

for i in range(N-1):
    fst, snd = map(int, sys.stdin.readline().split())
    nodes[fst].append(snd)
    nodes[snd].append(fst)


def dfs(i:int):
    visit[i] = 1

    for num in nodes[i]:
        if not visit[num]:
            parents[num] = i
            dfs(num)

dfs(1)

print(*parents[2:], sep='\n')