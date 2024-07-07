import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())
MAX_SIZE = 100000
position = [-1 for _ in range(MAX_SIZE + 1)]  # -1: not visit, else : sec


def BFS(position, N, K):
    position[N] = 0
    queue = deque([N])

    while queue:
        now = queue.popleft()
        if now == K:
            print(position[now])
            return
        next_cost = position[now] + 1
        points = [now + 1, now - 1, now * 2]

        for p in points:
            if 0 <= p <= MAX_SIZE and position[p] == -1:
                queue.append(p)
                position[p] = next_cost

BFS(position, N, K)