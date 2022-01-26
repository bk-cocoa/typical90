from itertools import groupby


N = int(input())
S = input()

# L<Rとした時のL,Rの全パターン
# L=Rのときは絶対条件満たさないからね
all_cnt = N * (N - 1) // 2

# oかx、どちらか1種類しか含まれない時答えは絶対0
if S.count('o') == 0 or S.count('x') == 0:
    print(0)
    exit()

ng_cnt = 0

# ランレングス圧縮
for s,v in groupby(S):
    s_cnt = len(list(v))
    if s_cnt != 1:
        ng_cnt += s_cnt*(s_cnt-1)//2

print(all_cnt - ng_cnt)