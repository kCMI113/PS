import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
K = int(input())
board = [[0 for _ in range(N)] for _ in range(N)]  # 1: body, 2: apple

for _ in range(K):
    x, y = map(int, input().split())
    board[x - 1][y - 1] = 2

L = int(input())
moves = [input().split() for _ in range(L)]
moves = {int(ele[0]): ele[1] for ele in moves}

snake = deque([[0, 0]])  # tail - head
board[0][0] = 1
cnt = 0
dir = 0  # 0~3: 오하왼상

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

while True:
    cnt += 1
    now_x, now_y = snake[-1][0] + dx[dir], snake[-1][1] + dy[dir]
    if not (0 <= now_x < N and 0 <= now_y < N) or board[now_x][now_y] == 1:
        print(cnt)
        break

    if board[now_x][now_y] != 2:
        tail_x, tail_y = snake.popleft()
        board[tail_x][tail_y] = 0

    snake.append([now_x, now_y])
    board[now_x][now_y] = 1

    if cnt in moves.keys():
        dir = (dir + 3) % 4 if moves[cnt] == "L" else (dir + 1) % 4

# 방향
# 0 -> 3  1
# 1 -> 0  2
# 2 -> 1  3
# 3 -> 2  0
