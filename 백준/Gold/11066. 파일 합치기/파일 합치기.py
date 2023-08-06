import sys

T = int(sys.stdin.readline().rstrip())


for t in range(T):
    K = int(sys.stdin.readline())
    files = list(map(int, sys.stdin.readline().split()))
    dp = [[0 for _ in range(K)] for _ in range(K)]
    sub_sum = [0 for _ in range(K+1)]
  

    for k in range(K):
        sub_sum[k] = sub_sum[k-1] + files[k]
    
    for size in range(1,K):
        for start in range(K-1):
            end = start + size

            if end >= K:
                break
            
            res = float("inf")
            for mid in range(start, end):
                res = min(res, dp[start][mid]+dp[mid+1][end] + sub_sum[end] - sub_sum[start-1])

            dp[start][end] = res
    print(dp[0][K-1])