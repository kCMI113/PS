import sys

query = list(sys.stdin.readline().rstrip())

if query[::-1] == query:
    print(1)
else:
    print(0)