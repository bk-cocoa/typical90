# 入力
N = int(input())
A_L = [list(map(int, input().split())) for i in range(N)]

mod = 10**9+7
ans = 1
for i in range(N):
    dice_sum = 0
    for j in range(6):
        dice_sum += A_L[i][j]
    ans *= dice_sum
    ans %= mod
print(ans)