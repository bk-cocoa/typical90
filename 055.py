# 入力
N, P, Q = map(int, input().split())
A_L = list(map(int, input().split()))
A_L.sort()
ans = 0

# 5秒に甘えて全探索
for a in range(N - 4):
    for b in range(a + 1, N - 3):
        for c in range(b + 1, N - 2):
            for d in range(c + 1, N - 1):
                for e in range(d + 1, N):
                    tmp = A_L[a]
                    tmp %= P
                    tmp *= A_L[b]
                    tmp %= P
                    tmp *= A_L[c]
                    tmp %= P
                    tmp *= A_L[d]
                    tmp %= P
                    tmp *= A_L[e]
                    tmp %= P
                    if tmp == Q:
                        ans += 1
print(ans)
