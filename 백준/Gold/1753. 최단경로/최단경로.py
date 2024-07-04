import heapq
import sys

input = sys.stdin.readline
INF = 1e9
v, e = map(int, input().split())
start = int(input())
dist = [INF] * (v + 1)
heap = []
graph = [[] for _ in range(v + 1)]


def Dijkstra(start):
    dist[start] = 0
    heapq.heappush(heap, (0, start))
    while heap:
        w, node = heapq.heappop(heap)
        if dist[node] < w:
            continue

        for next in graph[node]:
            cost = next[0] + w
            if cost < dist[next[1]]:
                dist[next[1]] = cost
                heapq.heappush(heap, (cost, next[1]))


for _ in range(e):
    x, y, z = map(int, input().split())
    graph[x].append((z, y))

Dijkstra(start)
for i in range(1, v + 1):
    print("INF" if dist[i] == INF else dist[i])
