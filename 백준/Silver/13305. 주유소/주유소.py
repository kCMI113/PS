N = int(input())
km = list(map(int,input().split()))
cost = list(map(int,input().split()))
now_oil = 0
tot_cost = 0

for i in range(N-1):
    if(now_oil < km[i]):
        if(cost[i] == min(cost[i:])):
            tot_cost += cost[i]*sum(km[i:])
            break
        elif(i+1<N and cost[i]<cost[i+1]):
            tot_cost += cost[i]*(km[i]+km[i+1])
            now_oil += (km[i]+km[i+1])
        else:
            tot_cost += cost[i]*km[i]
            now_oil += km[i]
    now_oil -= km[i]
    
print(tot_cost)