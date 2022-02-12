from collections import deque

# 入力
H, W = map(int, input().split())
sr, sc = tuple(map(int, input().split()))
gr, gc = tuple(map(int, input().split()))
# 壁は上下左右に番兵置きたい…
glid = [['#'] * (W + 2)]
for i in range(H):
    tmp = ['#'] + list(input()) + ['#']
    glid.append(tmp)
glid.append(['#'] * (W + 2))

# 移動先リスト
move_L = [(1, 0), (-1, 0), (0, 1), (0, -1)]

inf = 10 ** 10
# その地点までの最小コスト
dist_L = [[inf] * (W + 2) for i in range(H + 2)]
dist_L[sr][sc] = 0

que = deque()
que.append((sr, sc))

while que:
    now_r, now_c = que.popleft()
    now_dist = dist_L[now_r][now_c]
    next_dist = now_dist + 1

    for dr, dc in move_L:
        next_r = now_r + dr
        next_c = now_c + dc

        while True:
            if glid[next_r][next_c] == '#' or dist_L[next_r][next_c] < next_dist:
                break

            que.append((next_r, next_c))
            dist_L[next_r][next_c] = next_dist
            next_r += dr
            next_c += dc

print(dist_L[gr][gc] - 1)