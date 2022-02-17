from collections import deque
import heapq

N, M = map(int, input().split())
edge_L = [[] for _ in range(N)]
for i in range(M):
    a, b, c = map(int, input().split())
    a, b = a - 1, b - 1
    edge_L[a].append((c, b))
    edge_L[b].append((c, a))

# 0からの各点の距離:ダイクストラ
inf = 10**18
dist_L = [inf]*N
heap_L = [(0,0)]
dist_L[0] = 0

while heap_L:
    cost,node = heapq.heappop(heap_L)

    if dist_L[node] < cost:
        continue

    for next_cost,next_node in edge_L[node]:
        if dist_L[node] + next_cost < dist_L[next_node]:
            dist_L[next_node] = dist_L[node] + next_cost
            heapq.heappush(heap_L,(dist_L[next_node],next_node))

# Nからの各点の距離：ダイクストラ
rev_dist_L = [inf]*N
heap_L = [(0,N-1)]
rev_dist_L[N-1] = 0

while heap_L:

    cost,node = heapq.heappop(heap_L)

    if rev_dist_L[node] < cost:
        continue

    for next_cost,next_node in edge_L[node]:
        if rev_dist_L[node] + next_cost < rev_dist_L[next_node]:
            rev_dist_L[next_node] = rev_dist_L[node] + next_cost
            heapq.heappush(heap_L,(rev_dist_L[next_node],next_node))

for i in range(N):
    print(dist_L[i]+rev_dist_L[i])