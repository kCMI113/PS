from collections import deque

N = int(input())
que = deque(range(1, N + 1))

while len(que) > 1:
    que.popleft()
    que.append(que.popleft())

print(que[0])
