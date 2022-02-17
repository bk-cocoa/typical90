import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import connected_components
from collections import defaultdict

# 入力
N, M = map(int, input().split())
edge = np.array([input().split() for _ in range(M)], dtype=np.int64).T

# 強連結成分分解
tmp = np.ones(M, dtype=np.int64).T
graph = csr_matrix((tmp, (edge[:] - 1)), (N, N))
cnt, connected_L = connected_components(graph, directed=True, connection='strong')

cnt_d = defaultdict(int)

ans = 0

for i in connected_L:
    cnt_d[i] += 1

for v in cnt_d.values():
    if v == 1:
        continue

    ans += v * (v - 1) // 2

print(ans)
