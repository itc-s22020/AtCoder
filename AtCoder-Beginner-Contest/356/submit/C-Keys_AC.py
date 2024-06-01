N, M, K = map(int, input().split())
t = []

for _ in range(M):
    l = input().split()
    C = int(l[0])
    k = list(map(int, l[1:C + 1]))
    r = l[C + 1]
    t.append((C, k, r))
rc = 0
for co in range(1 << N):
    V = True
    for C, k, r in t:
        c = sum(1 for key in k if co & (1 << (key - 1)))
        if (r == 'o' and c < K) or (r == 'x' and c >= K):
            V = False
            break
    if V:
        rc += 1
print(rc)

