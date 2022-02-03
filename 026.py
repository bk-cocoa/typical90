from collections import deque

# 入力
from typing import List, Any

N = int(input())
edge_L = [[] for i in range(N)]
for i in range(N - 1):
    A, B = map(int, input().split())
    A, B = A - 1, B - 1
    edge_L[A].append(B)
    edge_L[B].append(A)

# 1:BFSで頂点0から各頂点までの距離取る：O(N+M)
# 2:頂点0からの距離が偶数/奇数で分ける：O(N)
# 3:多い方適当にN/2個だけ並べたら良さそう？
# 結果：計算量：

# BFSやってみる
que = deque()
que.append(0)
check_L = [0] * N # 0:未チェック、+-1：奇数偶数分け
check_L[0] = 1

# BFS!!!!!
while que:
    node = que.popleft()
    next_node_L = edge_L[node]
    next_node: int
    for next_node in next_node_L:
        if check_L[next_node] != 0:
            continue
        check_L[next_node] = check_L[node] * (-1)
        que.append(next_node)

# 赤と青で分けてみた
red_L = []
blue_L = []

for i in range(N):
    color = check_L[i]
    if color == 1:
        red_L.append(i + 1)
    else:
        blue_L.append(i + 1)

# 個数が長い方を使って、N/2個だけ並べる
if len(red_L) > len(blue_L):
    print(*red_L[:N // 2])
else:
    print(*blue_L[:N // 2])
