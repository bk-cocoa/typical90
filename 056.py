N, S = map(int, input().split())
A_L = []
B_L = []
for i in range(N):
    A, B = map(int, input().split())
    A_L.append(A)
    B_L.append(B)

dp = [[False] * (S + 1) for _ in range(N + 1)]
dp[0][0] = True

for day in range(N):
    for price in range(S):
        if dp[day][price]:
            if price + A_L[day] <= S:
                dp[day + 1][price + A_L[day]] = True
            if price + B_L[day] <= S:
                dp[day + 1][price + B_L[day]] = True

if not dp[-1][-1]:
    print('Impossible')
    exit()

price = S
ans_L = []

for day in range(N, 0, -1):

    if price >= A_L[day - 1] and dp[day - 1][price - A_L[day - 1]]:
        ans_L.append('A')
        price -= A_L[day - 1]
    else:
        ans_L.append('B')
        price -= B_L[day - 1]
print(''.join(ans_L[::-1]))
