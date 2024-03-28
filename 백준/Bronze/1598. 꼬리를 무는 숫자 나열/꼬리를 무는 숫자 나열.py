import sys

num1, num2 = map(int, sys.stdin.readline().rstrip().split())
num1 -= 1
num2 -= 1

print(abs(num1 // 4 - num2 // 4) + abs(num1 % 4 - num2 % 4))
