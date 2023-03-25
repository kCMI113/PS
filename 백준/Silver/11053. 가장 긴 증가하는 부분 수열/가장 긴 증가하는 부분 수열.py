n = int(input())
nums = list(map(int, input().split()))

res = [1 for _ in range(n+1)]

for i in range(n):
    for j in range(i):
        if nums[i]>nums[j]:
            res[i] = max(res[i], res[j]+1)
print(max(res))
