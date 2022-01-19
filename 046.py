from collections import defaultdict

# 入力
N = int(input())
A_L = list(map(int, input().split()))
B_L = list(map(int, input().split()))
C_L = list(map(int, input().split()))

# 「余りがxになる要素の数」で管理してあげたい：defaultdictで集計する
# lambdaで綺麗に入力→dictまで持っていける…？:TODO

A_d = defaultdict(int)
B_d = defaultdict(int)
C_d = defaultdict(int)
for i in range(N):
    A_d[A_L[i] % 46] += 1
    B_d[B_L[i] % 46] += 1
    C_d[C_L[i] % 46] += 1

ans = 0

for a in range(46):
    for b in range(46):
        for c in range(46):

            if (a+b+c)%46==0:
                # それぞれのあまりの和が46の倍数となるような選び方なんで積を求めてカウント
                tmp = A_d[a]*B_d[b]*C_d[c]
                ans += tmp
print(ans)
