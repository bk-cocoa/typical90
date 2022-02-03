from collections import defaultdict
from collections import deque

# 入力
N = int(input())
root_d = defaultdict(set)
for _ in range(N - 1):
    A, B = map(lambda x: int(x) - 1, input().split())
    root_d[A].add(B)
    root_d[B].add(A)

# 方針：BFSで最長点を2回求めてプラス1
length_l = [-1] * N
length_l[0] = 0
que = deque()
que.append(0)
max_length = 0
max_length_node = 0

# 1:都市0から一番遠いところを探すよ
while que:
    node = que.popleft()  # 今見てる場所
    next_s = root_d[node]  # 今見てる場所から行ける場所一覧

    next_length = length_l[node] + 1  # 都市0から、次に行く場所への距離

    for next_node in next_s:
        if length_l[next_node] == -1:
            length_l[next_node] = next_length
            if max_length < next_length:
                max_length_node = next_node
                max_length = next_length
            que.append(next_node)

length_l = [-1] * N
length_l[max_length_node] = 0
que.append(max_length_node)
max_length = 0
max_length_node = 0

# 1:「都市0から一番遠い都市」から一番遠いところを探すよ
while que:
    node = que.popleft()  # 今見てる場所
    next_s = root_d[node]  # 今見てる場所から行ける場所一覧

    next_length = length_l[node] + 1  # 都市0から、次に行く場所への距離

    for next_node in next_s:
        if length_l[next_node] == -1:
            length_l[next_node] = next_length
            if max_length < next_length:
                max_length_node = next_node
                max_length = next_length

            que.append(next_node)

print(max_length + 1)