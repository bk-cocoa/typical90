# 入力
N = int(input())
A_L = [list(map(int, input().split())) for i in range(N)]
M = int(input())
XY_L = [list(map(int, input().split())) for i in range(M)]
NG_L = [set() for i in range(N)]

for x,y in XY_L:
    x -= 1
    y -= 1
    NG_L[x].add(y)
    NG_L[y].add(x)

import itertools
perms = list(itertools.permutations(range(N)))

ans = 10 ** 9

for perm in perms:
    NG_flg = True
    for i in range(N-1):
        if perm[i+1] in NG_L[perm[i]]:
            NG_flg = False
            break

    if NG_flg:
        tmp = 0
        for i in range(N):
            tmp += A_L[perm[i]][i]
        ans = min(ans,tmp)

if ans == 10**9:
    print(-1)
else:
    print(ans)