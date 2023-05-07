add = 0
diff = 1
mul = 2
div = 3

n = int(input())
nums = list(map(int,input().split()))
oprt = list(map(int,input().split()))
min_res, max_res  = int(1e9), -int(1e9)

def dfs(cnt, val, n_add, n_diff, n_mul, n_div):
    global max_res, min_res
    if cnt == n:
        max_res = max(max_res,val)
        min_res = min(min_res,val)
        return
    else:
        if n_add:
            dfs(cnt+1, val + nums[cnt], n_add-1, n_diff, n_mul, n_div)
        if n_diff:
            dfs(cnt+1, val - nums[cnt], n_add, n_diff-1, n_mul, n_div)
        if n_mul:
            dfs(cnt+1, val * nums[cnt], n_add, n_diff, n_mul-1, n_div)
        if n_div:
            dfs(cnt+1, int(val / nums[cnt]), n_add, n_diff, n_mul, n_div-1)

dfs(1, nums[0], oprt[add], oprt[diff], oprt[mul], oprt[div])
print(max_res)
print(min_res)