# https://www.acmicpc.net/problem/14719
import sys

h, w = map(int, sys.stdin.readline().rstrip().split())
blocks = list(map(int, sys.stdin.readline().rstrip().split()))
res = 0

for now in range(1, w - 1):  # 양 끝은 물을 채울 수 없으므로 탐색하지 않음
    l = blocks.index(max(blocks[:now]))  # now의 좌측에서 벽 찾기
    r = blocks.index(max(blocks[now + 1 :]))  # now의 우측에서 벽 찾기

    water = min(blocks[l], blocks[r]) - blocks[now]
    if water > 0:
        res += water

print(res)
