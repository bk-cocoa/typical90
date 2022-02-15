from collections import deque
import copy

# 入力
H, W = map(int, input().split())
glid_L = [['#'] * (W + 2)]
for _ in range(H):
    tmp_L = ['#'] + list(input()) + ['#']
    glid_L.append(tmp_L)
glid_L.append(['#'] * (W + 2))

# 例外は外す
if H == 1 or W == 1:
    print(-1)
    exit()

dx_L = [1, 0, -1, 0]
dy_L = [0, 1, 0, -1]

# スタート地点全探索したい
ans = -1
for start_H in range(1, H + 1):
    for start_W in range(1, W + 1):

        # 山からスタートはしません
        if glid_L[start_H][start_W] == '#':
            continue

        # ここでどうにか解きたい
        # H,W,これまでに通った経路でbfs?
        que = deque()
        road_s = set()
        road_s.add((start_H, start_W))
        que.append((start_H, start_W, road_s))

        while que:

            now_H, now_W, now_road_s = que.popleft()

            for dx, dy in zip(dx_L, dy_L):
                next_H = now_H + dx
                next_W = now_W + dy

                road_s = copy.copy(now_road_s)
                if (next_H, next_W) == (start_H, start_W) and 3 <= len(road_s):
                    ans = max(ans,len(road_s))
                    continue

                if (next_H, next_W) in road_s:
                    continue

                if glid_L[next_H][next_W] == '#':
                    continue


                road_s.add((next_H,next_W))
                que.append((next_H,next_W,road_s))


print(ans)
