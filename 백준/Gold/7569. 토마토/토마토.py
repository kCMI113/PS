import sys
from collections import deque

def bfs() -> None:
    while que:
        now_x, now_y, now_z = que.popleft()
        now_tmt = MAP[now_z][now_x][now_y]

        for i in range(6):
            new_x = now_x+dx[i]
            new_y = now_y+dy[i]
            new_z = now_z+dz[i]

            if 0<=new_x<N and 0<=new_y<M and 0<=new_z<H :
                if MAP[new_z][new_x][new_y] == 0:
                   que.append((new_x, new_y, new_z))
                   MAP[new_z][new_x][new_y] = now_tmt+1
                

M,N,H = map(int, sys.stdin.readline().split())
MAP = [[list(map(int, sys.stdin.readline().split())) for _ in range(N)] for _ in range(H)]
dx = [-1, 0, 0, 1, 0, 0]
dy = [0, -1, 0, 0, 1, 0]
dz = [0, 0, -1, 0, 0, 1]
que = deque()

for h in range(H):
    for n in range(N):
        for m in range(M):
            if MAP[h][n][m] == 1:
                que.append((n,m,h))

bfs()
MAP = set([ele for threedim in MAP for twodim in threedim for ele in twodim])

if 0 in MAP:
    print(-1)
else:
    print(max(MAP)-1)