# 入力
N = int(input())
A_L = list(map(int, input().split()))
B_L = list(map(int, input().split()))

# 夫々ソートして、
A_L.sort()
B_L.sort()

# 左から順番に入れていく感じ
ans = 0
for i in range(N):
    ans += abs(A_L[i] - B_L[i])

print(ans)