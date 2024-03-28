import sys

row, col = map(int, sys.stdin.readline().rstrip().split())
print(col - 1 + col * (row - 1))
