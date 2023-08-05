import sys
from collections import deque

def bfs(x:int, y:int, graph: list[list[int]]) -> int:
    dx = [-1,0,1,0]
    dy = [0,-1,0,1]
    que = deque()

    que.append((x,y))
    
    while que:
        x, y = que.popleft()
        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]
            if(-1<new_x<N and -1<new_y<M):
                if(graph[new_x][new_y] == 1):
                    graph[new_x][new_y] = graph[x][y]+1
                    que.append((new_x, new_y))

    return graph[N-1][M-1]

N, M = map(int, sys.stdin.readline().split())
graph = []

for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().rstrip())))

print(bfs(0,0,graph))