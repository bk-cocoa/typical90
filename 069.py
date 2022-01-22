# 入力
N, K = map(int, input().split())

mod = 10 ** 9 + 7

# コーナーケースの処理
if N == 1:
    print(K)
    exit()
if K < 2:
    print(0)
    exit()

# 通常時の計算
ans = K * (K - 1)
ans %= mod
ans *= pow(K - 2, N - 2, mod)
ans %= mod
print(ans)
