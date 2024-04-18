import sys

word = list(sys.stdin.readline().rstrip())
print(int(word == word[::-1]))