N = int(input())
km = list(map(int,input().split()))
cost = list(map(int,input().split()))
tot_cost = 0
min_cost = cost[0]

for i in range(len(km)):
    min_cost = min(min_cost, cost[i])
    tot_cost += min_cost*km[i]
    
print(tot_cost)

