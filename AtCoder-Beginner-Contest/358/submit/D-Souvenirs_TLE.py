from collections import defaultdict
n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
d = defaultdict(list)
for i in range(n):d[a[i]].append(i)
b.sort()
c = 0
s = 0
U = float('inf')

for p in sorted(d.keys()):
    if s == m:break
    for i in d[p]:
        e = a[i]
        for j in range(s, m):
            if b[j] <= e:
                c += p
                s += 1
                U = min(U, b[j])
                break
        if s == m:
            break

print([c, -1][s < m])
