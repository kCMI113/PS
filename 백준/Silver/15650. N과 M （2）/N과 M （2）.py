N, M = map(int, input().split())

res = set()
nums = set()


def backtracking(nums):
    if len(nums) == M:
        res.add(" ".join(map(str, sorted(nums))))

    for num in range(1, N + 1):
        if num not in nums:
            nums.add(num)
            backtracking(nums)
            nums.remove(num)


backtracking(nums)
print("\n".join(sorted(res)))
