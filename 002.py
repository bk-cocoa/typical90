N = int(input())
ans_L = []

# Nが奇数のときは打ち切り
if N % 2 != 0:
    print()
    exit()

# 2^N回ループ回して（＝N桁の2進数を全探索）
for i in range(2 ** N):
    tmp_s = bin(i)[2:].zfill(N)

    # 左括弧と右括弧の数が合ってないのは打ち切り
    if tmp_s.count('1') != tmp_s.count('0'):
        continue

    cnt = 0
    OK_flg = True

    # 左括弧より右括弧のほうが先に来たら打ち切り
    for s in tmp_s:
        if s == '1':
            cnt += 1
        else:
            cnt -= 1

        if cnt < 0:
            OK_flg = False
            break

    # 大丈夫なら、解答として確保
    if OK_flg:
        ans_L.append(tmp_s.replace('1','(').replace('0',')'))

# ソート忘れずに
ans_L.sort()
for s in ans_L:
    print(s)