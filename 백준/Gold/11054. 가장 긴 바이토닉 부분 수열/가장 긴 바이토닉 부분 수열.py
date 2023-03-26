n = int(input())
nums = list(map(int, input().split()))
nums_rev = nums[::-1]

min_res = [1 for _ in range(n)]
max_res = [1 for _ in range(n)]
tot_res = [0 for _ in range(n)]

for i in range(n):
    for j in range(i):
        if nums[i]>nums[j]: #정방향
            max_res[i] = max(max_res[i], max_res[j]+1) 
        if nums_rev[i] > nums_rev[j]: #역방향
            min_res[i] = max(min_res[i], min_res[j]+1)
    
min_res = min_res[::-1]
for i in range(n):
    tot_res[i] = max_res[i]+min_res[i]-1

print(max(tot_res))