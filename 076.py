from collections import deque

# 入力
N = int(input())
A_L = [a*1000 for a in map(int, input().split())]


print(A_L)
exit()

size_sum = sum(A_L)  # 合計値出しとく
A_L = A_L + A_L  # 円形なので、ループの辻褄合わせ：Nと1の境界を跨いだ時のために2週させちゃう
que = deque() # 確保した区間をqueで管理
que_sum = 0 # 毎回sum出すの手間なので、appendしたら足す、popしたら引くよ
target_num = size_sum // 10 # queの中身がこれになったら正解！

# A_Lの左から順にqueに入れていく
for a in A_L:
    que.append(a)
    que_sum += a # que_sumもappendする時に足すの忘れずに！

    # 目標値(合計値の1/10)とqueの中身が等しくなったら終わり！
    if target_num == que_sum:
        print('Yes')
        exit()

    # queの中身が目標値超えちゃったら、左端から1個ずつ捨てていくよ
    while que_sum > size_sum // 10 and len(que) > 0:
        que_sum -= que.popleft()

# 2週試してみてもダメなら、No。おわり。
print('No')
