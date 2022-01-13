# 入力
N = int(input())
a, b, c = map(int, input().split())
ans = 10000

# 全探索の高速化
for a_cnt in range(10000):
    for b_cnt in range(10000):

        # a、bの枚数が決まっていればcの枚数はループさせなくても決まるよね
        # 3重ループが2重ループになった！はやい！
        if N < a * a_cnt + b * b_cnt:
            break
        if (N - (a * a_cnt + b * b_cnt)) % c == 0:
            tmp_ans = a_cnt + b_cnt + ((N - (a * a_cnt + b * b_cnt)) // c)
            ans = min(ans, tmp_ans)
print(ans)
