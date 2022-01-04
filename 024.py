# 入力
N, K = map(int, input().split())
A_L = list(map(int, input().split()))
B_L = list(map(int, input().split()))

# 1~Nまで、先頭から1つずつ比較して、絶対値の差を集計する
diff = 0
for i in range(N):
    a = A_L[i]
    b = B_L[i]
    diff += abs(a - b)

# 絶対値の差がK以下 かつ、偶奇が一緒ならYes
if diff <= K and diff % 2 == K % 2:
    ans = 'Yes'
else:
    ans = 'No'

print(ans)