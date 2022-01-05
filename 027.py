# 入力
N = int(input())

regist_S = set() # 登録済みの一覧をセットで管理
for i in range(1,N+1): # 日にちなんで1〜N+1に直す
    S = input()

    if S not in regist_S: # もし登録していない名前であれば
        regist_S.add(S) # 登録して
        print(i) # 日にちを出力
