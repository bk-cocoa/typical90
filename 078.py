import bisect

# 入力
N, M = map(int, input().split())
G = [[] for i in range(N)]
for i in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    G[a].append(b)
    G[b].append(a)

ans = 0

# それぞれの隣接点をソートして、にぶたんで左に要素が1つあればカウント
for i in range(N):
    tmp_L = G[i]
    tmp_L.sort()
    if bisect.bisect(tmp_L, i) == 1:
        ans += 1

print(ans)
