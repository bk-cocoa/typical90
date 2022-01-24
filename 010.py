# 入力
N = int(input())

# 組ごとに学籍番号分の点数配列用意
# 同じ学籍番号の生徒は存在しないので、1組に存在する生徒の学籍番号は、2組だと0点で問題無し
P1_L = [0] * N
P2_L = [0] * N

# どっちの組か判断して、学籍番号の場所に点数を格納していく
for i in range(N):
    C, P = map(int, input().split())
    if C == 1:
        P1_L[i] = P
    else:
        P2_L[i] = P

# 累積和を作る（O(N))->これで質問Q個（クエリ）に対して、O(1)で解答できる。すごい。
# 頭に0入れるとか、indexがずれるとかはお好みで補正
accum1_L = [0]
accum2_L = [0]
for i in range(N):
    accum1_L.append(accum1_L[-1]+P1_L[i])
    accum2_L.append(accum2_L[-1]+P2_L[i])

# クエリ部分
for _ in range(int(input())):

    # 1組累積和、2組累積和から欲しい部分を抜き出して解答
    L,R = map(int,input().split())
    ans1 = accum1_L[R] - accum1_L[L-1]
    ans2 = accum2_L[R] - accum2_L[L-1]
    print(ans1,ans2)