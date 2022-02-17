from collections import defaultdict

# 入力
N, K = map(int, input().split())

def push_a(x: int) -> int:
    return (x + sum(map(int, list(str(x))))) % (10 ** 5)

# N=0なら何回押しても0
if N == 0:
    print(0)
    exit()

# Kが大きくないなら、直接回してしまえホトトギス
if K < 10**6:
    for _ in range(K):
        N = push_a(N)
    print(N)
    exit()

# ループが存在する場合、ループの回数を数えるよ
checked_d = defaultdict(int)
loop_cnt = 0
while True:
    if checked_d[N] != 0:
        loop_cnt -= checked_d[N]
        break
    checked_d[N] = loop_cnt
    N = push_a(N)
    loop_cnt += 1

# ループを減らしたい
# ループに入るまでの数＝checked_d[N]
# 10**6回数のループを3回くらいマージンで回すつもりの計算
K -= (K // loop_cnt-3) * loop_cnt + checked_d[N]

for _ in range(K):
    N = push_a(N)

print(N)