# 入力
L, R = map(int, input().split())

L_cnt = 0
R_cnt = 0
mod = 10 ** 9 + 7

L-=1
for i in range(1,len(str(L)) + 1):
    start = 10 ** (i - 1)
    end = 10 ** i - 1

    if L < end:
        end = L

    cnt = i * (start % mod + end % mod) * (end % mod - start % mod + 1) // 2
    cnt %= mod
    L_cnt += cnt


for i in range(1,len(str(R)) + 1):
    start = 10 ** (i - 1)
    end = 10 ** i - 1

    if R < end:
        end = R

    cnt = i * (start % mod + end % mod) * (end % mod - start % mod + 1) // 2
    cnt %= mod
    R_cnt += cnt



print((R_cnt - L_cnt)%mod)