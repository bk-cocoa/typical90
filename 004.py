# 入力
H, W = map(int, input().split())
L = []
row_sum_L = [0] * H
col_sum_L = [0] * W

for row in range(H):
    tmp_L = list(map(int, input().split()))
    L.append(tmp_L)
    # 入力しながら行毎の合計、列毎の合計を取っていって…
    row_sum_L[row] = sum(tmp_L)
    for col in range(W):
        col_sum_L[col] += tmp_L[col]

# 行の合計 + 列の合計 - マスの値 = 答え
for row in range(H):
    ans_L = []
    for col in range(W):
        ans = row_sum_L[row] + col_sum_L[col] - L[row][col]
        ans_L.append(ans)
    print(*ans_L)
