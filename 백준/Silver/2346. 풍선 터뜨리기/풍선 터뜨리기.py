import sys
from collections import deque

input = sys.stdin.readline
N = int(input())
bolls = list(map(int, input().split()))
que = deque([i for i in range(1, N + 1)])

for _ in range(N):
    idx = que.popleft()
    print(idx, end=" ")
    step = 1 - bolls[idx - 1] if bolls[idx - 1] > 0 else -1 * bolls[idx - 1]
    que.rotate(step)
