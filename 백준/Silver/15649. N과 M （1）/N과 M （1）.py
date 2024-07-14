N, M = map(int, input().split())
res = []

def backtracking(res):
    if len(res) == M:
        print(" ".join(map(str, res)))
        return

    for num in range(1, N + 1):
        if num not in res:
            res.append(num)
            backtracking(res)
            res.pop()

backtracking(res)