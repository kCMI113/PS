import sys
from collections import deque

def bfs(x:int, y:int) -> int:
    cnt = 1
    que = deque([(x,y)])
    MAP[x][y] = 0

    while que:
        now_x, now_y = que.popleft()
        for i in range(4):
            new_x = now_x+dx[i]
            new_y = now_y+dy[i]

            if 0<=new_x<N and 0<=new_y<N and MAP[new_x][new_y]:
                cnt += 1
                MAP[new_x][new_y] = 0
                que.append((new_x,new_y))

    return cnt

N = int(sys.stdin.readline())
MAP = []
res = []
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

for _ in range(N):
    line = list(map(int, sys.stdin.readline().rstrip()))
    MAP.append(line)

for x in range(N):
    for y in range(N):
        if MAP[x][y]:
            res.append(bfs(x,y))

res.sort()
print(len(res))

for num in res:
    print(num)