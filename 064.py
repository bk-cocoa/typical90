# 入力
N,Q = map(int,input().split())
A_L = list(map(int, input().split()))

# 初期状態での不便さを求める
# 初期状態の不便さと、地殻変動後の不便さのずれは、
# L[i]とL[i]-1の間、R[i]とR[i]+1の間でしか発生しないので
# クエリ解く時はそこだけ求めて誤差補正してあげればO(1)で済むはず…

# 初期状態での不便さを求めてみる
score = 0
score_L = []
for i in range(N-1):
    tmp = A_L[i+1]-A_L[i]
    score += abs(tmp)
    score_L.append(tmp)


for i in range(Q):
    L,R,V = map(int,input().split())

    if 1 < L:
        L -= 2
        score -= abs(score_L[L])
        score_L[L] += V
        score += abs(score_L[L])
    if R < N:
        R -= 1
        score -= abs(score_L[R])
        score_L[R] -= V
        score += abs(score_L[R])
    print(score)
