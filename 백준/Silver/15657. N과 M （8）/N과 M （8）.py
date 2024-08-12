N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))
res = []


def backtracking(start):
    if len(res) == M:
        print(*res, sep=" ")
        return

    for i in range(start, N):
        res.append(nums[i])
        backtracking(i)
        res.pop()


backtracking(0)
