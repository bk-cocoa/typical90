from collections import deque

# 入力
N, Q = map(int, input().split())
A_L = list(map(int, input().split()))

# これ以降、全クエリをキューで殴るための意思表明
que = deque(A_L)

# Q回クエリをぶんなぐる
for i in range(Q):

    # クエリ受け取って
    t, x, y = map(int, input().split())
    # 0-indexになおして
    x -= 1
    y -= 1

    # 1ならすわっぷ！
    if t == 1:
        que[x], que[y] = que[y], que[x]
    # 2ならローテ！
    elif t == 2:
        que.rotate(1)
    # 3でほしい所出力！
    elif t == 3:
        print(que[x])
