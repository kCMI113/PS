import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))
que = deque([i for i in range(1, n + 1)])
cnt = 0

for num in nums:
    while que[0] != num:
        if que.index(num) < len(que) / 2:
            que.rotate(-1)
        else:
            que.rotate(1)
        cnt += 1
    que.popleft()

print(cnt)
