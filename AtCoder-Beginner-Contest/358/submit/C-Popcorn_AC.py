import itertools

N, M = map(int, input().split())
S = [set(j for j, t in enumerate(input().strip()) if t == 'o') for _ in range(N)]
a, r = set(range(M)), float('inf')

for i in range(1, N + 1):
    for c in itertools.combinations(S, i):
        u = set()
        for k in c:u.update(k)
        if u == a:
            r = min(r, i)
            break
    if r != float('inf'):break
print(r)


