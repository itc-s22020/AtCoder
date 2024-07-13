N = int(input())
LR = [tuple(map(int, input().split())) for _ in range(N)]
X = [L for L, R in LR]
t, a, c = 0, [], sum(X)
for i in range(N):
    L, R = LR[i]
    a.append((L, R, X[i]))
for i in range(N):
    if c == t:
        break
    L, R, cv = a[i]
    if c < t:
        diff = min(t - c, R - cv)
        X[i] += diff
        c += diff
    elif c > t:
        diff = min(c - t, cv - L)
        X[i] -= diff
        c -= diff
if c == t:
    print("Yes")
    print(" ".join(map(str, X)))
else:
    print("No")

