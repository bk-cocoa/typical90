# 入力
K = int(input())

mod = 10**9+7

if K %9 != 0:
    print(0)
    exit()

dp = [0]*(K+20)
dp[1] = 1
dp[2] = 1
dp[3] = 1
dp[4] = 1
dp[5] = 1
dp[6] = 1
dp[7] = 1
dp[8] = 1
dp[9] = 1
for i in range(1,K+1):

    cnt = dp[i]
    cnt %= mod

    for j in range(1,10):
        next_cnt = i+j


        dp[next_cnt] += cnt
        dp[next_cnt] %= mod

print(dp[K])