N, M = map(int, input().split())
h = list(map(int, input().split()))

for i in range(N):
    if M >= h[i]:
        M -= h[i]
    else:
        print(i)
        break
else:print(N)