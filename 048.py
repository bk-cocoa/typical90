import heapq

# 入力
N, K = map(int, input().split())

part_l = []
all_l = []

for i in range(N):
    A, B = map(int, input().split())
    # 大きい順に取りたいのでマイナス掛けて、問題番号管理もしたいのでタプルで
    part_l.append((-B, i))
    all_l.append((B - A, i))

heapq.heapify(part_l) # ひーぷきゅー

cnt = 0 # かけた時間
ans = 0 # 獲得点数
ac_s = set() # 解いた問題

while cnt < K:
    # 部分点獲得可能な問題の中で、一番部分点が高いものを取り出して1分使って解く
    score, question = heapq.heappop(part_l)
    ans += (-1) * score
    cnt += 1

    # もし、今解いた問題が部分点だけ（1分しか使ってない）なら、後半の残り1分かけて獲得可能な点数をヒープキューに追加する
    if question not in ac_s:
        ac_s.add(question)
        heapq.heappush(part_l, all_l[question])

print(ans)
