import sys

input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))  # que: 0, stack: 1
B = list(map(int, input().split()))
M = int(input())
C = list(map(int, input().split()))
que = []

for i in range(N - 1, -1, -1):
    if not A[i]:
        que.append(B[i])

que += C
print(*que[:M], sep=" ")
