N, K = map(int, input().split())
A = list(map(int, input().split()))

o = K
c = 0

for v in A:
    if v <= o:
        o -= v
    else:
        c += 1
        o = K - v

if o < K:
    c += 1

print(c)
