# 入力
N = int(input())
S = input()
mod = 10 ** 9 + 7
check_L = ['a', 't', 'c', 'o', 'd', 'e', 'r']
# 例外を除外する
for s in check_L:
    if S.count(s) == 0:
        print('No')
        exit()

check_L = ['0', 'a', 't', 'c', 'o', 'd', 'e', 'r']

# dpスタンバイ！
dp = [[0] * (N + 1) for _ in range(8)]
dp[0][0] = 1

for pos in range(1,N+1):
    s = S[pos-1]

    for i in range(8):
        if check_L[i] == s:
            dp[i][pos] = dp[i][pos-1] + dp[i-1][pos-1]
            dp[i][pos] %= mod
        else:
            dp[i][pos] = dp[i][pos-1]

print(dp[-1][-1]%mod)