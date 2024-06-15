N, A = map(int, input().split())
T = list(map(int, input().split()))
F = 0
for i in range(0, N):
    if T[i] < F:F += A
    else:F = T[i] + A
    print(F)
