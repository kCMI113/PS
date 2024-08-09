import sys

input = sys.stdin.readline
N, M = map(int, input().rstrip().split())
keyword = set(input().rstrip() for _ in range(N))

for _ in range(M):
    keyword -= set(input().rstrip().split(","))
    print(len(keyword))
