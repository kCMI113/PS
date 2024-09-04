import sys
from collections import deque

input = sys.stdin.readline

a, b = map(int, input().split())


def BFS(node):
    que = deque([[node, 1]])

    while que:
        now, cost = que.popleft()
        if now == a:
            return cost

        next = []
        if now % 2 == 0:
            next.append(now // 2)
        if now % 10 == 1:
            next.append(now // 10)
        
        for num in next:
            if 1 <= num <= b:
                que.append([num, cost + 1])
    return -1

print(BFS(b))
