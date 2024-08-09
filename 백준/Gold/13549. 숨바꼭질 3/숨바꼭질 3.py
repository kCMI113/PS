import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())
MAX_SIZE = 100000
position = [-1 for _ in range(MAX_SIZE + 1)]


def BFS(N, K):
    position[N] = 0
    que = deque([N])

    while que:
        now = que.popleft()
        if now == K:
            print(position[now])
            return
        costs = [0, 1, 1]
        points = [now, -1, +1]

        for i in range(3):
            new = now + points[i]
            if 0 <= new <= MAX_SIZE and position[new] == -1:
                if i == 0:
                    que.appendleft(new)
                else:
                    que.append(new)
                position[new] = position[now] + costs[i]


BFS(N, K)
