N, M = map(int, input().split())

res = []


def backtracking(i):
    if len(res) == M:
        print(" ".join(map(str, res)))
        return

    for num in range(i, N + 1):
        if num not in res:
            res.append(num)
            backtracking(num + 1)
            res.pop()


backtracking(1)
