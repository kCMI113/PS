import sys

num1, num2 = map(int, sys.stdin.readline().rstrip().split())
col1, row1 = 0, 0
col2, row2 = 0, 0

if num1 % 4 == 0:
    col1 = num1 // 4
    row1 = 4
else:
    col1 = num1 // 4 + 1
    row1 = num1 % 4

if num2 % 4 == 0:
    col2 = num2 // 4
    row2 = 4
else:
    col2 = num2 // 4 + 1
    row2 = num2 % 4

print(abs(col1 - col2) + abs(row1 - row2))
