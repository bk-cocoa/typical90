import bisect
# 入力
N = int(input())
A_L = list(map(int, input().split()))

# 番兵として、最小値と最大値を入れてソート。にぶたん用
A_L.append(-10**18)
A_L.append(10**18)
A_L.sort()

# クエリ処理
Q = int(input())
for i in range(Q):
    B = int(input())

    # にぶたんで入るところと、その隣を求めて…
    idx1 = bisect.bisect_left(A_L, B)
    idx2 = idx1-1
    # それぞれの不満度を計算、小さい方を出力！
    diff1 = abs(A_L[idx1] - B)
    diff2 = abs(A_L[idx2] - B)
    print(min(diff1, diff2))
