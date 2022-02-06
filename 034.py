from collections import deque
from collections import defaultdict

N, K = map(int, input().split())
A_L = list(map(int, input().split()))

ans_cnt = 0
check_cnt = 0
que = deque()
d = defaultdict(int)
ans = 0
for a in A_L:

    if d[a] == 0:
        check_cnt += 1
        ans_cnt += 1
        d[a] += 1
        que.append(a)
    else:
        ans_cnt += 1
        d[a] += 1
        que.append(a)

    while check_cnt > K:
        del_num = que.popleft()
        ans_cnt -= 1
        d[del_num] -= 1
        if d[del_num] == 0:
            check_cnt -= 1

    ans = max(ans,ans_cnt)
print(ans)