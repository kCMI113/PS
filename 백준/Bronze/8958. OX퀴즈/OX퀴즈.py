import sys

n = int(sys.stdin.readline())

for _ in range(n):
    ox = sys.stdin.readline()
    res = []
    for i in range(len(ox)):
        if ox[i] == "X":
            res.append(0)
        if ox[i] == "O":
            if res:
                res.append(res[-1] + 1)
            else:
                res.append(1)
    print(sum(res))
