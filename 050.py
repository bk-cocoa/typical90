# 入力
N, L = map(int, input().split())
mod = 10 ** 9 + 7
# DP配列準備して…
dp = [0] * (N + 1)
dp[0] = 1  # 初期化

for i in range(N):
    dp[i + 1] += dp[i]
    dp[i + 1] %= mod
    if i + L <= N:
        dp[i + L] += dp[i]
        dp[i + L] %= mod

print(dp[-1])
