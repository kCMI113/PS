import sys

input = sys.stdin.readline

T = int(input())
testcase = [int(input()) for _ in range(T)]
MAX_n = min(max(testcase), 10000) + 1
dp = [1 for _ in range(MAX_n)]

for i in range(2, MAX_n):
    dp[i] += dp[i - 2]

for i in range(3, MAX_n):
    dp[i] += dp[i - 3]


print(*[dp[n] for n in testcase], sep="\n")
