N, M = map(int, input().split())
C = input().split()
D = input().split()
P = list(map(int, input().split()))
defaultP = P.pop(0)
total = 0
for c in C:
    if c in D:
        for i,d in enumerate(D):
            if c == d:
                total+=P[i]
                break
    else:
        total+=defaultP
print(total)
