N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))
res = []


def backtracking():
    if len(res) == M:
        print(*res, sep=" ")
        return

    for i in range(N):
        if nums[i] not in res:
            res.append(nums[i])
            backtracking()
            res.pop()


backtracking()
