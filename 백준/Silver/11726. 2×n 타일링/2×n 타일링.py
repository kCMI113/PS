# https://www.acmicpc.net/problem/11726

import sys

n = int(sys.stdin.readline())
dp = [0 for _ in range(n if n > 2 else 2)]
dp[0], dp[1] = 1, 2

for i in range(2, n):
    dp[i] = (dp[i - 1] + dp[i - 2])

print(dp[n - 1] % 10007)
