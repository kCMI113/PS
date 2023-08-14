import sys
from collections import deque

def bfs():
    while que:
        now_x, now_y = que.popleft()
        now_tmt = MAP[now_x][now_y]

        for i in range(4):
            new_x = now_x+dx[i]
            new_y = now_y+dy[i]

            if 0<=new_x<N and 0<=new_y<M and MAP[new_x][new_y] == 0 :
                   que.append((new_x, new_y))
                   MAP[new_x][new_y] = now_tmt+1
                

M, N = map(int, sys.stdin.readline().split())
MAP = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
que = deque()

for n in range(N):
    for m in range(M):
        if MAP[n][m] == 1:
            que.append((n,m))

bfs()
MAP = set([ele for onedim in MAP for ele in onedim])

if 0 in MAP:
    print(-1)
else:
    print(max(MAP)-1)