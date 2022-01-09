# 入力
N8, K = map(str, input().split())


# 10進数を、b進数に変換するための関数
def base10to(n, b):
    if n // b:
        return base10to(n // b, b) + str(n % b)
    return str(n % b)


# 一旦10進数に直してから9進数に変換する
for i in range(int(K)):
    N10 = int(N8, 8)
    N9 = base10to(N10, 9)
    N8 = N9.replace('8', '5')

print(N8)
