n = int(input())
li = []
for i in range(n):
    _ = input()
    li.append([i+1,list(map(int, input().split()))])
R = int(input())
S = []
for v in li:
    if R in v[1]:S.append(v)
V = 999
for K in S:
    if V > len(K[1]):
        V = len(K[1])
M = []
for H in S:
    if len(H[1]) == V:
        M.append(H[0])
print(len(M))
print(*M)
