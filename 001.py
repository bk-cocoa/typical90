N, L = map(int, input().split())
K = int(input())
A_L = list(map(int, input().split()))

def make_piece_l(L: list, length: int) -> list:
    return_l = []
    tmp_length = 0

    for a in L:
        return_l.append(a - tmp_length)
        tmp_length = a
    return_l.append(length - L[-1])

    return return_l

def calc_score(n: int) -> bool:
    return_l = []
    score = 0
    for a in A_L:
        score += a
        if score >= n:
            return_l.append(score)
            score = 0

    return len(return_l) > K

A_L = make_piece_l(A_L, L)
l, r = 0, L

while r - l > 1:
    mid = (l + r) // 2

    if calc_score(mid):
        l = mid
    else:
        r = mid

print(l)



