import sys

input = sys.stdin.readline
k = int(input())
path = list(map(int, input().split()))
res = [[] for _ in range(k)]

depth = 0
l = 0
r = len(path)


def find(depth, l, r):
    if l >= r:
        return
    mid = (l + r) // 2
    res[depth].append(path[mid])
    find(depth + 1, l, mid)
    find(depth + 1, mid + 1, r)


find(depth, l, r)
for nums in res:
    for num in nums:
        print(num, end=" ")
    print()
