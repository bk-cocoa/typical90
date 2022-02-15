# 入力
K = int(input())

ans = 0

for a in range(1,K+1):

    if a*a*a > K:
        break

    if K % a != 0:
        continue

    for b in range(a,K+1):
        if a*b*b > K:
            break

        if K % b != 0:
            continue

        if K % (a * b) == 0:
            ans += 1

print(ans)