import sys
import heapq

n = int(sys.stdin.readline())
abs_heap = []

for i in range(n):
    query = int(sys.stdin.readline())
    
    if query>0:
        heapq.heappush(abs_heap, (query,query))
    elif query<0:
        heapq.heappush(abs_heap, (-1*query,query))
    elif abs_heap:
        print(heapq.heappop(abs_heap)[-1])
    else:
        print(0)