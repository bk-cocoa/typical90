from collections import deque

# 入力
N = int(input())
edge_L = [[] for _ in range(N)]
for i in range(N - 1):
    A, B = map(lambda x: int(x) - 1, input().split())
    edge_L[A].append(B)
    edge_L[B].append(A)

# 1: BFSで頂点0から各頂点までの距離取る： O(N+N)
# 2: 多い方適当に N/2 個だけ並べたら良さそう？
# 結果 計算量:O(N)

# BFSやってみる
que = deque([0])
check_L = [0] * N # 0:未チェック、+-1：奇数偶数分け
check_L[0] = 1

# BFS!!!!! & 赤と青で分けてみた
red_L, blue_L = [1], []
while que:
    node = que.popleft()
    for next_node in edge_L[node]:
        if check_L[next_node] == 0:
            check_L[next_node] = -check_L[node]
            if check_L[next_node] == 1:
                red_L.append(next_node + 1)
            else:
                blue_L.append(next_node + 1)
            que.append(next_node)

# 個数が長い方を使って、N/2個だけ並べる
if len(red_L) > len(blue_L):
    print(*red_L[:N // 2])
else:
    print(*blue_L[:N // 2])