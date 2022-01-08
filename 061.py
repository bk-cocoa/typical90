from collections import deque

# 入力
Q = int(input())

que = deque()

for i in range(Q):
    t, x = map(int, input().split())
    if t == 1:
        que.appendleft(x)
    if t == 2:
        que.append(x)
    if t == 3:
        print(que[x - 1])
