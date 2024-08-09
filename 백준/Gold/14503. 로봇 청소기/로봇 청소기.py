import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
r, c, d = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visit = [[0 for _ in range(m)] for _ in range(n)]


def BFS(i, j, d):
    visit[i][j] = 1
    que = deque([[i, j]])
    cnt = 1
    dx = [-1, 0, 1, 0]  
    dy = [0, 1, 0, -1]

    while que:
        now_x, now_y = que.popleft()
        empty = 0

        for _ in range(4):
            d = (d + 3) % 4
            new_x = now_x + dx[d]
            new_y = now_y + dy[d]

            if 0 <= new_x < n and 0 <= new_y < m and not graph[new_x][new_y] and not visit[new_x][new_y]:
                visit[new_x][new_y] = 1
                que.append([new_x, new_y])
                cnt += 1
                empty = 1
                break

        if not empty:
            if not graph[now_x - dx[d]][now_y - dy[d]]:  # 후진
                que.append([now_x - dx[d], now_y - dy[d]])
            else:
                return cnt


print(BFS(r, c, d))
