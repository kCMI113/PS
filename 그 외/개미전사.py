# 개미 전사는 메뚜기 마을의 창고 공격, 창고는 일직선으로 이어져있음. 
# 각 창고에는 정해진 수의 식량을 저장하고 있고 개미전사는 선택적으로 창고를 약탈함. 
# 메뚜기 정찰병은서로 인접한 창고가 공격받으면 바로 알 수 있음. 즉!! 최소한 한 칸 이상 떨어진 창고를 약탈해야함

n = int(input())
array = list(map(int, input().split()))
d = [0]*100

d[0] = array[0]
d[1] = max(array[0], array[1])

for i in range(2,n):
    d[i] = max(d[i-2]+array[i], d[i-1])

print(d[n-1])