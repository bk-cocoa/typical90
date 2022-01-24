import bisect

# 入力
N, M = map(int, input().split())
G = [[] for _ in range(N)]
for i in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    G[a].append(b)
    G[b].append(a)


# それぞれの隣接点をソートして、にぶたんで左に要素が1つあればカウント
ans = 0
for i in range(N):
    tmp_L = sorted(G[i])
    if bisect.bisect(tmp_L, i) == 1:
        ans += 1

print(ans)