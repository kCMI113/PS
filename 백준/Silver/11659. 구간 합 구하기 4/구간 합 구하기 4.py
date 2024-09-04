import sys

input = sys.stdin.readline
N, M = map(int, input().split())
nums = list(map(int, input().split()))
ijs = [list(map(int, input().split())) for _ in range(M)]
max_n = max([ele for _, ele in ijs])
dp = [0 for _ in range(max_n + 1)]

for i in range(1, max_n + 1):
    dp[i] = dp[i - 1] + nums[i - 1]

for i, j in ijs:
    print(dp[j] - dp[i - 1])
