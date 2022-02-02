from collections import defaultdict

# UnionFind
# uf = UnionFind(N)
#   N:ノード数（0~N-1)
# parents():各要素の親番号の番号を格納するリストを返す。要素が根(ルート)の場合は-(そのグループの要素数)を格納
# find(x):要素xが属するグループの根を返す
# union(x,y):要素xが属するグループと要素yが属するグループを併合する
# size(x):要素xが属するグループのサイズ（要素数）を返す
# same(x):要素xと要素yが同じグループに属するかどうかを返す
# members(x):要素xが属するグループに属する要素をリストで返す
# roots():全ての根の要素をリストで返す
# group_count():グループの数を返す
# all_group_members():dictで全てのグループの全ての要素を返す

class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members

    def __str__(self):
        return '\n'.join(f'{r}: {m}' for r, m in self.all_group_members().items())

# 入力
H,W = map(int,input().split())
Q = int(input())

uf = UnionFind(30000000)
red_s = set()
side_L = [-10000,1,10000,-1]

#クエリ
for i in range(Q):
    query = list(map(int, input().split()))

    # 1:塗りつぶし
    if query[0] == 1:
        r,c = query[1],query[2]
        cell_num = r*10000+c
        red_s.add(cell_num)

        for i in side_L:
            side_cell_num = cell_num+i
            if side_cell_num in red_s:
                uf.union(side_cell_num,cell_num)

    # 2:出力
    else:
        a = query[1]*10000+query[2]
        b = query[3]*10000+query[4]

        if uf.same(a,b) and a in red_s and b in red_s:
            print('Yes')
        else:
            print('No')

