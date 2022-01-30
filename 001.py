N, L = map(int, input().split())
K = int(input())
A_L = list(map(int, input().split()))


def make_piece_l(L,length):
    return_l = []
    tmp_length = 0

    for a in L:
        return_l.append(a - tmp_length)
        tmp_length = a
    return_l.append(length - L[-1])
    return return_l


def calc_score(n):
    return_l = []
    score = 0
    for a in A_L:
        score += a
        if score >= n:
            return_l.append(score)
            score = 0

    if len(return_l) > K:
        return True
    else:
        return False


A_L = make_piece_l(A_L,L)
l = 0
r = L

while True:
    mid = (l + r)//2
    if r == mid or l == mid:
        print(mid)
        break
    if calc_score(mid):
        l = mid
    else:
        r = mid
