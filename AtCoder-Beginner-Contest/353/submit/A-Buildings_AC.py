N = int(input())
H = list(map(int, input().split()))
f = H[0]

for i,v in enumerate(H):
    if v > f:
        print(i + 1)
        break
else:
    print(-1)
