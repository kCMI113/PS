import sys

def calc(a:int, b:int, c:int, dp:list[list[list[int]]])->int:
    if min(a,b,c) <= 0:
        return dp[0][0][0]
    if max(a,b,c) >= 21:
        return calc(20,20,20,dp)
    if dp[a][b][c]:
        return dp[a][b][c]
    if a<b<c:
        dp[a][b][c] = calc(a,b,c-1,dp) + calc(a,b-1,c-1,dp) - calc(a,b-1,c,dp)
    else:
        dp[a][b][c] = calc(a-1,b,c,dp) + calc(a-1,b-1,c,dp) + calc(a-1,b,c-1,dp) - calc(a-1, b-1,c-1,dp)

    return dp[a][b][c]

dp = [[[0 for _ in range(21)] for _ in range(21)] for _ in range(21)] 
dp[0][0][0] = 1

while True:
    a,b,c = map(int,sys.stdin.readline().split())
    if set([a,b,c]) == set([-1]): 
        break
    print("w({}, {}, {}) = {}".format(a,b,c,calc(a,b,c,dp)))