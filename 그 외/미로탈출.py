# **미로탈출 : BFS 이용**
# NxM 미로, 입구(1,1)에서 출구(N,M)로 가야함. 한 번에 한 칸씩 이동할 수 있으며 괴물(0이 있는 칸)을 피해서 탈출해야함

# (****************아이디어****************)

# 1. 각 노드의 최소 거리를 구해주면 된다.

def pri(length):
    for i in range(n):
        for j in range(m):
            print(length[i][j], end=" ")
        print()

n, m = map(int, input().split())
graph = []
length = []

for i in range(n):
    graph.append(list(map(int, input())))
    length.append([1e7]*m) #큰 값으로 초기화

length[0][0] = 1
dx = [-1,0,1,0]     #좌상우하
dy = [0,-1,0,1]

for i in range(n):
    for j in range(m):
        # pri(length)
        # print("+++++++++++++++")
        for k in range(4):
            newx = i + dx[k]
            newy = j + dy[k]
            newlen = length[i][j] +1
            if newx<0 or newx>= n or newy<0 or newy>=m: #범위를 벗어남
                continue
            if graph[newx][newy] == 0: #괴물이 존재하는 곳
                continue
            if(length[newx][newy] > newlen): # 새로운 경로의 길이가 더 작은 경우만 변경
                length[newx][newy] = newlen


print(length[n-1][m-1])