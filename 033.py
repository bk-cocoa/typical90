# 入力
H, W = map(int, input().split())

if 2<=H and 2<=W:
    H = -(-H//2)
    W = -(-W//2)

print(H*W)