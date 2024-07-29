import sys

input = sys.stdin.readline
S = input().rstrip()
T = input().rstrip()


def solve(s, t):
    if s == t:
        print(1)
        sys.exit()
    if len(s) > len(t):
        return
    if t[0] == "B":
        solve(s, t[1:][::-1])
    if t[-1] == "A":
        solve(s, t[:-1])
    return


solve(S, T)
print(0)
