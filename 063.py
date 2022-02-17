from collections import defaultdict

# 入力
H, W = list(map(int, input().split()))
P_L = [list(map(int, input().split())) for _ in range(H)]

# Hが最大8なので、bit全探索で行を全通り詰める(2^8=256)
# 1つも選ばないパターンは無いので、1から
ans = 0

for i in range(1, 2 ** H):
    check_L = []

    for j in range(H):
        # その行を選ぶ時
        if (i >> j) & 1:
            check_L.append(P_L[j])

    cnt_d = defaultdict(int)
    row_cnt = len(check_L)
    ng_flg = True
    for w in range(W):
        check_num = check_L[0][w]
        if row_cnt == 1:
            cnt_d[check_num] += row_cnt
            continue

        for h in range(1, row_cnt):
            if check_L[h][w] != check_num:
                break
        else:
            cnt_d[check_num] += row_cnt

    if len(cnt_d):
        max_v = max(cnt_d.values())
        ans = max(max_v, ans)

print(ans)