import math

# 入力
T = int(input())
L, X, Y = map(int, input().split())

# E分後に、E8君の乗っているゴンドラががどの座標(0,y,z)に居るかを計算して…
# ゴンドラのx,y座標と高橋像の座標から、直線距離出して…
# 水平距離(dist)と垂直距離(z)が分かるので、arctan(z/dist)で角度が出る、はず…。

# クエリ処理部
Q = int(input())
for i in range(Q):
    E = int(input())

    # 1.ゴンドラの座標計算
    ## 1.1. E8くんが乗ってから何周してる？
    time = E/T
    ## 1.2. time分乗ったら観覧車は何度動いた？
    rad = math.pi * 2 * time
    ## x座標は0なので、y座標、z座標を求める
    z = (L/2) - math.cos(rad)*(L/2)
    y = (L/2) * math.sin(rad)*(-1)

    # 2:x,y平面上の、高橋像とゴンドラの距離を求める
    dist = math.dist([X,Y],[0,y])

    # 3:distとzから、arctanやってみる
    # rad→deg忘れずに。
    print(math.degrees(math.atan(z/dist)))