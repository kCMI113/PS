N, M = map(int, input().split())

res = []


def backtracking(i):
    if len(res) == M:
        print(" ".join(map(str, res)))
        return

    for num in range(i, N + 1):
        res.append(num)
        backtracking(num)
        res.pop()


backtracking(1)
