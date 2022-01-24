# 入力
N = int(input())
A_L = [list(map(int, input().split())) for i in range(N)]

mod = 10**9+7
ans = 1
for i in range(N):
    dice_sum = sum([A_L[i][j] for j in range(6)])
    ans *= dice_sum
    ans %= mod

print(ans)