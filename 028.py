import pprint
from collections import defaultdict

# 入力
N = int(input())

# いもすリスト準備
imos_L = [[0] * 1005 for _ in range(1005)]

# 紙毎にポイント（左下、右上）を取得
for a in range(N):
    lx, ly, rx, ry = map(int, input().split())

    imos_L[lx][ly] += 1
    imos_L[lx][ry] -= 1
    imos_L[rx][ly] -= 1
    imos_L[rx][ry] += 1

accum_L = []

# 横向きに累積和取って…
for i in range(len(imos_L)):
    tmp_L = [0]
    for j in imos_L[i]:
        tmp_L.append(tmp_L[-1]+j)
    accum_L.append(tmp_L)

# 転地して縦向きにいもす。その時に重なってる枚数を辞書管理してあげて
T_accum_L = list(zip(*accum_L))
ans_d = defaultdict(int)
max_cnt = 0
for i in range(len(T_accum_L)):
    tmp_cnt = 0
    for j in T_accum_L[i]:
        cnt = tmp_cnt+j
        ans_d[cnt] += 1
        max_cnt = max(max_cnt,cnt)
        tmp_cnt = cnt

# 辞書出力
for i in range(1,N+1):
    print(ans_d[i])