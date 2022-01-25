# 入力
H, W = map(int, input().split())
A_L = [list(map(int, input().split())) for _ in range(H)]
B_L = [list(map(int, input().split())) for _ in range(H)]

cnt = 0
for r in range(H - 1):
    for c in range(W - 1):
        diff = B_L[r][c] - A_L[r][c]
        cnt += abs(diff)

        A_L[r][c] += diff
        A_L[r+1][c] += diff
        A_L[r][c+1] += diff
        A_L[r+1][c+1] += diff

if A_L == B_L:
    print('Yes')
    print(cnt)
else:
    print('No')