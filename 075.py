N = int(input())

# 素数判定とか素因数分解とか
# 試し割り法

def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a

prime_L = prime_factorize(N)
prime_cnt = len(prime_L)
base_L = []

# にぶたん？って思ったけどにぶたんするまでもなかった（10**12個素数が並んだとしても50個くらい）
for i in range(N):
    check_num = 2**i
    if prime_cnt <= check_num:
        print(i)
        exit()
