# 入力
H, W = map(int, input().split())

row_sum_L, col_sum_L = [0] * H, [0] * W
L = []
for row in range(H):
    L.append(list(map(int, input().split())))
    # 入力しながら行毎の合計、列毎の合計を取っていって…
    row_sum_L[row] = sum(L[-1])
    for col in range(W):
        col_sum_L[col] += L[-1][col]

# 行の合計 + 列の合計 - マスの値 = 答え
for row in range(H):
    ans_L = []
    for col in range(W):
        ans = row_sum_L[row] + col_sum_L[col] - L[row][col]
        ans_L.append(ans)
    print(*ans_L)