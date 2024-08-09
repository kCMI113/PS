import sys

input = sys.stdin.readline
N = int(input())
nums = list(map(int, input().split()))
M = int(input())
res = 0


def calcul(lim):
    temp = 0
    for num in nums:
        if num > lim:
            temp += lim
        else:
            temp += num
    return temp


if sum(nums) <= M:
    res = max(nums)
else:
    l_idx, r_idx = 1, max(nums)
    while l_idx <= r_idx:
        mid = (l_idx + r_idx) // 2
        if calcul(mid) > M:
            r_idx = mid - 1
        else:
            l_idx = mid + 1
            res = mid

print(res)
