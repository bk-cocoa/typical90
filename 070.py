# 入力
import statistics

N = int(input())
X_L, Y_L = [], []
for _ in range(N):
    X, Y = map(int, input().split())
    X_L.append(X)
    Y_L.append(Y)

med_X = statistics.median(X_L)
med_Y = statistics.median(Y_L)

print(int(sum([abs(X_L[i] - med_X) + abs(Y_L[i] - med_Y) for i in range(N)])))