import sys

point_x = []
point_y = []
res = []

for _ in range(3):
    x,y = map(int, sys.stdin.readline().split())
    point_x.append(x)
    point_y.append(y)

for x in set(point_x):
    if point_x.count(x) < 2:
        res.append(x)
for y in set(point_y):
    if point_y.count(y) < 2:
        res.append(y)

print(*res, sep=" ")