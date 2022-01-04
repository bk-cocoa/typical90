import math
# 入力
A,B,C = map(int,input().split())

# 3辺の長さの最大公約数を求める
gcd = math.gcd(A,math.gcd(B,C))

# それぞれの辺に対して、最大公約数で割ったものから1引いたものの和が答え
ans = (A+B+C)//gcd-3

print(ans)