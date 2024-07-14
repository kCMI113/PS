N, M = map(int, input().split())

res = []


def backtracking():
    if len(res) == M:
        print(" ".join(map(str, res)))
        return

    for num in range(1, N + 1):
        res.append(num)
        backtracking()
        res.pop()


backtracking()
